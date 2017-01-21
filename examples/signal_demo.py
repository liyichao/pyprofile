#!/usr/bin/env python
# coding: utf-8

import signal, traceback


def sample(_, frame):
    stack = traceback.format_stack(frame)



def f():
    j = 0
    for i in range(20):
        j += 1

def g():
    j = 0
    for i in range(10):
        j += 1


def main():
    while True:
        f()
        g()


