#Sum square difference

def sum_square():
    """
    returns: sum of squares of natural numbers 1-100
    """
     sumsq = [s**2 for s in range(1,101)]
     return sum(sumsq)

def square_sum():
    """
    returns: square of sum of natural numbers 1-100
    """
    sqsum = [s for s in range(1,101)]
    return (sum(sqsum))**2

def diff():
    """
    returns: difference between previous functions
    """
    return square_sum() - sum_square()

print(diff())
