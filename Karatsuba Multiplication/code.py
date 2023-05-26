def karatsuba(x, y):
    """
    Computes the product of two numbers using the Karatsuba algorithm.
    """
    # Base case
    if x < 10 or y < 10:
        return x * y
    
    # Determine the number of digits in the input numbers
    m = min(len(str(x)), len(str(y)))
    m2 = m // 2
    
    # Split the input numbers into two halves
    high1, low1 = x // 10 ** m2, x % 10 ** m2
    high2, low2 = y // 10 ** m2, y % 10 ** m2
    
    # Recursively compute the three products needed for the Karatsuba formula
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    
    # Apply the Karatsuba formula to obtain the final product
    return z2 * 10 ** (2 * m2) + (z1 - z2 - z0) * 10 ** m2 + z0
