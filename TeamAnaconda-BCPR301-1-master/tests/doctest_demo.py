"""
>>> 1 + 2
3

>>> a = 3
>>> print(a)
3

>>> list(range(34)) #doctest: +NORMALIZE_WHITESPACE
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 32,
 33]

>>> list(range(34)) #doctest: +ELLIPSIS
[0, 1, 2, ..., 33]

>>> 3/0 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
ZeroDivisionError: division by zero
"""


def fun1(a, b):
    """
    >>> fun1(2, 3)
    6
    """
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
