#!/usr/bin/python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

from novaprinter import prettyPrinter

class BtlibraryParser(HTMLParser):
    def __init__(self, keyword):
        super().__init__()
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
        if step == 'starttag' && args[0] == 'div':
            attrs = dict(args[1])
            if attrs.get('class') == 'item-title':
                self.state = self.item_title_state
            elif attrs.get('class') == 'item-detail':
                self.state = self.item_detail_state

    def item_title_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def desc_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def name_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def item_detail_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def link_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def time_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def size_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def count_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def speed_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':

    def leech_state(self, step, *args):
        if step == 'starttag':
        elif step == 'endtag':
        elif step == 'data':


class btlibrary(object):
    url = 'http://btlibrary.cc'
    name = 'BT Library'

    def __init__(self):
        self.parser = BtlibraryParser()

    def search_test(self, data):
        for d in self.parser.feed(data):
            prettyPrinter(d)

    def search(self, what, cat='all'):
        pass


if __name__ == "__main__":
    t = btlibrary()
    with open('btl_src', 'rb') as f:
        t.search_test(f.read())
    # t.search('modern+family')

