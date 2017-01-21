#!/usr/bin/env python
# coding: utf-8
"""WSGI server example"""
from __future__ import print_function
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()
import urllib2

read_times = 1


def f():
    for i in range(read_times):
        response = urllib2.urlopen('http://www.baidu.com', timeout=10)
    return response


def g():
    for i in range(2 * read_times):
        response = urllib2.urlopen('http://www.baidu.com', timeout=10)
    return response


def application(env, start_response):
    if env['PATH_INFO'] == '/':
        f()
        g()
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"<b>hello world</b>"]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [b'<h1>Not Found</h1>']


if __name__ == '__main__':
    print('Serving on 8088...')
    WSGIServer(('', 8088), application).serve_forever()
