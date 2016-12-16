#Smallest multiple

from math import gcd
from functools import reduce

def lcm(a,b):
    """
    a, b: integers
    returns: least common multiple of a and b.
    """
    return a*b//gcd(a,b)

print(reduce(lcm, range(1,21)))
