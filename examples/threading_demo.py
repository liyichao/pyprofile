#!/usr/bin/env python
# coding: utf-8

import threading


def g():
    j = 0
    for i in range(100):
        j += 1
    return j


def f():
    while True:
        g()


def f1():
    while True:
        g()

t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f1)
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
t1.join()


