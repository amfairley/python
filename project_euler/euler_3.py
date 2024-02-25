# Largest prime factor of 600851475143

# Factors of 600851475143
factors = []
target = 100012
for i in range(1,target):
    if target % i == 0:
        factors.append(i)

# Function to determine if a value is prime
def is_prime(x):
    factor_list = []
    for i in range (1,x):
        if x % i == 0:
            factor_list.append(i)
    if len(factor_list) == 1:
        return True
    else:
        return False

prime_factors = []
# For each value in the factors list
for i in factors:
    if is_prime(i):
        prime_factors.append(i)

print(max(prime_factors))



