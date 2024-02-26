def is_prime(x):
    """A simple function that determines whether an input integer is prime or not"""
    factor_list = []
    for i in range (1,x):
        if x % i == 0:
            factor_list.append(i)
    if len(factor_list) == 1:
        return True
    else:
        return False
    


def divisible(n,x,y):
    """A simple function that takes an integer input n, and outputs if it is divisible by a range of x-y"""
    # Range of items to divide by
    divisors = list(range(x,y+1))
    # Double check of divisors
    print(divisors)
    numbers = []
    for i in divisors:
        if n % i == 0:
            numbers.append(i)
    # If divisible by all the numbers return true
    if len(numbers) == len(divisors):
        return True
    else:
        return False

