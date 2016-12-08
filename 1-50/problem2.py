#Even Fibonacci numbers

def fib(base1, base2):
    """
    base1, base2: starting fibonacci numbers
    returns: int that is sum of even fibonacci numbers less than 4000000
    """
    if base1 > 4000000:
        return 0
    x = base1
    if x % 2 != 0:
        x = 0
    return x + fib(base2, base1 + base2)

fib(1,2)
