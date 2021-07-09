# Python BaseMath
A very simple library that allows you to do math in essentially any base.

# Installation
Since it's so simple -- and probably buggy at the moment -- I won't be putting it up on PyPI right now.
```
> python -m pip install wheel
> python -m pip install https://github.com/megamaz/pythonBaseMath/releases/download/1.0.0/BaseMath-1.0.0-py3.whl
```

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