#!/usr/bin/env python
# encoding: utf-8

def reduce2(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    >>> reduce2(mul, [2, 4, 8], 1)
    64
    >>> reduce2(pow, [1, 2, 3, 4], 2)
    16777216
    """
    for x in s:
        initial = f(initial, x)
    return initial

class Fib:

    def __init__(self, value=0):
        self.value = value

    """
    0 1 2 3 4 5
    0 1 1 2 3 5
     1 0 1 1 2

    """
    def next(self):
        if self.value == 0:
            self.difference = 1
        self.value, self.difference = self.value + self.difference, self.value
        return self

    def __repr__(self):
        return str(self.value)


class Bank:

    def __init__(self, holder, value):
        self.holder = holder
        self.balance = value

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            return "There is insufficient value now."
        self.balance -= value



class MissManners:
    """A container class that only forwards messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'

    >>> m = MissManners(v)
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        "*** YOUR CODE HERE ***"
        str = message.split(' ', 1)
        cmd = str[1]
        if not hasattr(self.obj, cmd):
            return "Thanks for asking, but I know not how to" + cmd
        return getattr(self.obj, cmd)(*args)


