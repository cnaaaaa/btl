#!/usr/bin/python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

from novaprinter import prettyPrinter
from helpers import retrieve_url

class BtlibraryParser(HTMLParser):
    def __init__(self):
        super(BtlibraryParser, self).__init__()
        self.state = self.init_state
        self.output = {}

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
        if step == 'endtag':
            if args[0] == 'div':
                self.state = self.init_state
        elif step == 'data':
            self.output['name'] = self.output.setdefault('name', '') + data

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
        if step == 'data':
            self.output['leech'] = data
            self.output['seeds'] = data


class btlibrary(object):
    url = 'http://btlibrary.cc'
    name = 'BT Library'

    def __init__(self):
        self.parser = BtlibraryParser()

    def search_test(self, data):
        for d in self.parser.feed(data):
            d['engine_url'] = url
            prettyPrinter(d)

    def search(self, what, cat='all'):
        pass


if __name__ == "__main__":
    t = btlibrary()
    with open('btl_src', 'rb') as f:
        t.search_test(f.read())
    # t.search('modern+family')

