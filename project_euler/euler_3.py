# Largest prime factor of 600851475143
def main():

    factors = []
    prime_factors = []
    target = 600851475143

    # Factors of 600851475143
    for i in range(1,target):
        if target % i == 0:
            factors.append(i)
    
        
    # Prime factors
    for i in factors:
        if is_prime(i):
            prime_factors.append(i)

    print(max(prime_factors))

# Functions:

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

if __name__ == "__main__":
    main()




