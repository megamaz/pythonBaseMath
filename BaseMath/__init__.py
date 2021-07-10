"""Allows you to do math in any base."""
from __future__ import annotations

import sys
import numpy
import contextlib
from io import StringIO
from typing import Union

from .exceptions import *

def _execWithOutput(code:str, stdout=None):
    try:
        old = sys.stdout
        if not stdout:
            stdout = StringIO()
        sys.stdout = stdout
        exec(f"r = {code}\nprint(r)")
        v = stdout.getvalue()
        sys.stdout = old
        
        return v
    except Exception as e:
        sys.stdout = old
        raise IncorrectExpression(f"Expression {code} is incorrect.") from e 
        # if you're here to find out why, thing is that I don't know either.

def _checkCanSymbolDoMath(a, b):
    if a.base != b.base:
        raise BaseDoesNotMatchError(f"Cannot do math on two numbers with differing bases. ({a.base} and {b.base})")

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
    
    def calculate(self, expression:str):
        values = [str(x) for x in range(10)] + [chr(x+65) for x in range(26)]
        for e in expression:
            if e not in values:
                continue

            if int(e, 36) > self.base:
                raise NumberOutOfBaseRange(f"Character {e} (number {int(e, 36)}) in expression is out of the base's range ({self.base}).")
        
        
        numInExpression = []
        num = ""
        for e in expression:
            if not (e in values):
                if num != "":
                    numInExpression.append(num.__str__())
                    num = ""
                continue
            else:
                num += e
            
        if num != "":
            numInExpression.append(num.__str__())

        newExpression = str(int(numInExpression[0], self.base))

        currentInd = 0
        expression = ''.join(expression.split())
        for e in expression:
            if e.upper() in values:
                continue
            else:
                currentInd += 1
                newExpression += e
                if currentInd == len(numInExpression):
                    break
                newExpression += str(int(numInExpression[currentInd], self.base))
        result = _execWithOutput(newExpression)
        return Symbol(int(result), self.base)

        


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
        if type(x) == Symbol:
            _checkCanSymbolDoMath(self, x)
        new = Symbol(int(x) + self.value, self.base)
        return new
    
    def __radd__(self, x):
        return self.__add__(x)
    
    def __sub__(self, x):
        if type(x) == Symbol:
            _checkCanSymbolDoMath(self, x)
        return Symbol(self.value - int(x), self.base)

    def __rsub__(self, x):
        return Symbol(int(x) - self.value, self.base)
    
    def __mul__(self, x):
        if type(x) == Symbol:
            _checkCanSymbolDoMath(self, x)
        return Symbol(int(x) * self.value, self.base)
    
    def __rmul__(self, x):
        return self.__mul__(x)

    def __div__(self, x):
        raise CannotDivideSymbols("Symbols cannot be divided.")
    
    def __rdiv__(self, x):
        return self.__div__(x)
    
    def __pow__(self, x):
        if type(x) == Symbol:
            _checkCanSymbolDoMath(self, x)
        return Symbol(self.value ** int(x), self.base)
    
    def __lt__(self, x):
        if type(x) == Symbol:
            if x.base != self.base:
                raise CannotCompareDifferingBases(f"Cannot compare two numbers with differing bases. ({self.base} and {x.base})")
        return self.value < int(x)
    
    def __gt__(self, x):
        if type(x) == Symbol:
            if x.base != self.base:
                raise CannotCompareDifferingBases(f"Cannot compare two numbers with differing bases. ({self.base} and {x.base})")
        return self.value > int(x)
    
    def __le__(self, x):
        if type(x) == Symbol:
            if x.base != self.base:
                raise CannotCompareDifferingBases(f"Cannot compare two numbers with differing bases. ({self.base} and {x.base})")
        return self.value <= int(x)
    
    def __ge__(self, x):
        if type(x) == Symbol:
            if x.base != self.base:
                raise CannotCompareDifferingBases(f"Cannot compare two numbers with differing bases. ({self.base} and {x.base})")
        return self.value >= int(x)
    
    def __eq__(self, x):
        if type(x) == Symbol:
            if x.base != self.base:
                raise CannotCompareDifferingBases(f"Cannot compare two numbers with differing bases. ({self.base} and {x.base})")
        return self.value == int(x)
    
    def __neg__(self):
        return -self.value