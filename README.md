# Python BaseMath
A very simple library that allows you to do math in essentially any base.

## Samples
1. Basic Usage
```py
>>> from BaseMath import Math
>>> math = Math(16)
>>> # assign a symbol to a variable
>>> A = math.symbol("A")
>>> A + 10
'14'
>>> B, C, D, E, F = math.symbol(*"B C D E F".split())
>>> A + B * E - B**2 
'2B'
>>> A * 10
'64'
```