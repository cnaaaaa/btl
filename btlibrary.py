#!/usr/bin/python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from urllib2 import urlopen, Request, re

from novaprinter import prettyPrinter
from helpers import retrieve_url

class BtlibraryParser(HTMLParser):
    def __init__(self, callback=None):
        HTMLParser.__init__(self)
        self.state = self.init_state
        self.output = {}
        self.callback = callback

    def handle_starttag(self, tag, attrs):
        self.state('starttag', tag, attrs)

    def handle_endtag(self, tag):
        self.state('endtag', tag)

    def handle_data(self, data):
        self.state('data', data)

    # fsm
    def init_state(self, step, *args):
        if step == 'starttag' and args[0] == 'div':
            attrs = dict(args[1])
            if attrs.get('class') == 'item-title':
                self.state = self.item_title_state
            elif attrs.get('class') == 'item-detail':
                self.state = self.item_detail_state

    def item_title_state(self, step, *args):
        if step == 'starttag':
            attrs = dict(args[1])
            self.output['desc_link'] = attrs.get('href')
            self.state = self.name_state

    def name_state(self, step, *args):
        if step == 'starttag':
            if args[0] == 'sup':
                self.state = self.init_state
        elif step == 'endtag':
            if args[0] == 'div':
                self.state = self.init_state
        elif step == 'data':
            self.output['name'] = self.output.setdefault('name', '') + args[0]

    def item_detail_state(self, step, *args):
        if step == 'starttag':
            if args[0] == 'a':
                attrs = dict(args[1])
                self.output['link'] = attrs.get('href')
                self.state = self.time_state

    def time_state(self, step, *args):
        if step == 'starttag':
            if args[0] == 'b':
                self.state = self.size_state

    def size_state(self, step, *args):
        if step == 'starttag':
            if args[0] == 'b':
                self.state = self.size_state2

    def size_state2(self, step, *args):
        if step == 'data':
            self.output['size'] = args[0]
            self.state = self.count_state

    def count_state(self, step, *args):
        if step == 'starttag':
            if args[0] == 'b':
                self.state = self.speed_state

    def speed_state(self, step, *args):
        if step == 'starttag':
            if args[0] == 'b':
                self.state = self.leech_state

    def leech_state(self, step, *args):
        if step == 'starttag':
            if args[0] == 'b':
                self.state = self.leech_state2

    def leech_state2(self, step, *args):
        if step == 'endtag':
            if args[0] == 'div':
                if self.callback:
                    self.callback(self.output)
                self.output = {}
                self.state = self.init_state
        if step == 'data':
            self.output['leech'] = self.output.setdefault('leech','') + args[0]
            self.output['seeds'] = self.output.setdefault('seeds','') + args[0]


class btlibrary(object):
    url = 'http://btlibrary.cc'
    name = 'BT Library'

    def __init__(self):
        self.parser = BtlibraryParser(self.callback)
        re_page = ''
        re_purl = ''

    def callback(self, d):
        d['engine_url'] = self.url
        prettyPrinter(d)

    def search_test(self, data):
        self.parser.feed(data)

    def parse(self, _url):
        bd = retrieve_url(_url)
        pages = int()
        purl = ''
        purl_t = ''
        if pages > 10:
            pages = 10
        for i in xrange(pages):
            purl = purl_t.format(i)
            bd = retrieve_url(purl)
            self.parser.feed(bd)

    def search(self, what, cat='all'):
        req = Request(url, {'keyword': what})
        resp = urlopen(req)
        if resp.code == 302:
            self.parse(resp.headers['location'])


if __name__ == "__main__":
    t = btlibrary()
    with open('btl_src', 'rb') as f:
        t.search_test(f.read())
    # t.search('modern+family')

