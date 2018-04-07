#!/usr/bin/env python
# encoding: utf-8


from lecture12 import *


def make_side(length, structure):
    return tree(length, [structure])


def length(s):
    return label(s)


def struct(s):
    return branches(s)[0]


def is_side(s):
    return type(label(s)) == int


def make_weight(value):
    return tree(value)


def weight(w):
    return label(w)


def is_weight(w):
    return is_leaf(w)


def make_mobile(left, right):
    return tree("mobile", [left, right])


def left_side(m):
    return branches(m)[0]


def right_side(m):
    return branches(m)[1]


def sides(m):
    return branches(m)

def is_mobile(m):
    return label(m) == "mobile"


def total_weight(m):
    if is_weight(m):
        return weight(m)
    else:
        weights = []
        for s in sides(m):
            side_struct = struct(s)
            side_weight = total_weight(side_struct)
            weights.append(side_weight)
        return sum(weights)

def side_torque(s):
    return length(s) * total_weight(struct(s))

def is_balanced(m):
    if is_weight(m):
        return weight(m)
    else:
        torques = []
        for s in sides(m):
            side_struct = struct(s)
            sid_length = length(s)
            torque = sid_length * total_weight(side_struct)
            torques.append(torque)
        return torques[0] == torques[1]


def example1():
    w1 = make_weight(5)
    w2 = make_weight(3)
    s1 = make_side(1, w1)
    s2 = make_side(2, w2)
    m1 = make_mobile(s1, s2)

    s3 = make_side(3, m1)
    s4 = make_side(4, w2)
    m = make_mobile(s3, s4)
    return m


def example2():
    w1 = make_weight(5)
    w2 = make_weight(3)
    s1 = make_side(1, w1)
    s2 = make_side(2, w2)
    m1 = make_mobile(s1, s2)

    s3 = make_side(3, m1)
    m = make_mobile(s3, s3)
    return m





