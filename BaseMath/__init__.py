"""Allows you to do math in any base."""
from __future__ import annotations

import numpy
from typing import Union
from . import exceptions
from .exceptions import *

class Math:

    def __init__(self, base):
        self.base = base

    def symbol(self, *val):
        r = []
        for x in val:
            r.append(
                Symbol(int(x, self.base), self.base)
            )
        if len(r) == 1:
            return r[0]

        return tuple(r)

class Symbol(object):

    value = 0
    base = 0

    def __init__(self, value, base):
        self.value = value
        self.base = base

    def __str__(self):
        return numpy.base_repr(self.value, self.base)

    def __repr__(self):
        return f"'{self.__str__()}'"

    def __int__(self):
        return self.value

    def __add__(self, x):
        new = Symbol(int(x) + self.value, self.base)
        return new
    
    def __radd__(self, x):
        return self.__add__(x)
    
    def __sub__(self, x):
        return Symbol(self.value - int(x), self.base)

    def __rsub__(self, x):
        return Symbol(int(x) - self.value, self.base)
    
    def __mul__(self, x):
        return Symbol(int(x) * self.value, self.base)
    
    def __rmul__(self, x):
        return self.__mul__(x)

    def __div__(self, x):
        raise CannotDivideSymbols("Symbols cannot be divided.")
    
    def __rdiv__(self, x):
        return self.__div__(x)
    
    def __pow__(self, x):
        return Symbol(self.value ** int(x), self.base)
    
    def __lt__(self, x):
        return self.value < int(x)
    
    def __gt__(self, x):
        return self.value > int(x)
    
    def __le__(self, x):
        return self.value <= int(x)
    
    def __ge__(self, x):
        return self.value >= int(x)
    
    def __eq__(self, x):
        return self.value == int(x)
    
    def __neg__(self):
        return -self.value
