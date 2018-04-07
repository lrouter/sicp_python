#!/usr/bin/env python
# encoding: utf-8


def tree(label, branches=[]):
    return [label] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def is_leaf(t):
    return not branches(t)
