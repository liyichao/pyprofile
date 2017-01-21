#!/usr/bin/env python
# coding: utf-8

import os
import gevent

MILLION = 1000 * 1000
print_interval = 1000
sleep_times = 10


def foo():
    for i in range(MILLION):
        if i % print_interval == 0:
            print("foo", i)
        for j in range(sleep_times):
            # Yield to the Gevent hub.
            gevent.sleep(0)


def bar():
    for i in range(MILLION):
        if i % print_interval == 0:
            print("bar", i)
        for j in range(2 * sleep_times):
            gevent.sleep(0)


def main():
    print("pid: ", os.getpid())
    foo_greenlet = gevent.spawn(foo)
    bar_greenlet = gevent.spawn(bar)
    foo_greenlet.join()
    bar_greenlet.join()

main()

