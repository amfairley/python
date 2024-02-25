# Checking if a value is prime:
def is_prime(x):
    factor_list = []
    for i in range (1,x):
        if x % i == 0:
            factor_list.append(i)
    if len(factor_list) == 1:
        return True
    else:
        return False