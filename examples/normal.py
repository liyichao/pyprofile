#!/usr/bin/env python
# coding: utf-8


def callee_d():
    j = 0
    for i in range(100):
        j += 1
    return j


def callee_a():
    callee_d()


def callee_b():
    callee_c()


def callee_c():
    callee_d()


def caller():
    callee_a()
    callee_b()
    callee_a()


while True:
    caller()
