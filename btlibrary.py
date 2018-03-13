#!/usr/bin/python

from HTMLParser import HTMLParser

from helpers import retrieve_url
from novaprinter import prettyPrinter

class BtlibraryParser(HTMLParser):
    def __init__(self, keyword):
        try:
            super().__init__()
        except:
            HTMLParser.__init__(self)
        self.keyword = keyword

        self.state

    def handle_starttag(self, tag, attrs):
        params = dict(attrs)

    def handle_endtag(self, tag):

    def handle_data(self, data):


class btlibrary(object):
    url = 'http://btlibrary.cc'
    name = 'BT Library'

    def search(self, what, cat='all'):
        pass


if __name__ == "__main__":
    t = btlibrary()
    t.search('modern+family')

