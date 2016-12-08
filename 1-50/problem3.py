#Largest prime factor

def prime_large(x):
    """
    x: integer
    returns: largest prime factor of x
    """
    a = 2
    num = x
    while True:
        if num % a == 0:
            c = a
            num /= a #dividing completely through removes smaller factors.
        if num == 1:
            return c
        else:
            a += 1

prime_large(600851475143)
