# Python BaseMath
A very simple library that allows you to do math in essentially any base.

# Installation
Since it's so simple -- and probably buggy at the moment -[-](https://www.youtube.com/watch?v=dQw4w9WgXcQ) I won't be putting it up on PyPI right now.
```
> python -m pip install wheel
> python -m pip install https://github.com/megamaz/pythonBaseMath/releases/download/1.1.0/BaseMath-1.1.0.whl
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
2. Math for bases smaller than 10
```py
>>> from BaseMath import Math
>>> math = Math(8)
>>> # there are many different names you could name your variables
>>> # for math with bases smaller than 10. You could go the spelled
>>> # version, with variables names one, two, three etc... or you
>>> # could go with _1, _2, _3 etc... Or, you could use math.calculate.
>>> # /!\ math.calculate USES EXEC, THIS COULD BE A CONCERN. /!\
>>> math.calculate("1 + 5 + 7")
'15'
>>>
```
3. Binary
```py
>>> from BaseMath import Math
>>> math = Math(2)
>>> math.calculate("10110 + 10110")
'101100'
```
