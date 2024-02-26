# Find the smallest positive number that is evenly divisible by all numbers from 1-20

def main():

    starting_value = 1
    ending_value = 20
    counter = 1

    while (divisible(counter, starting_value, ending_value) == False):
        counter += 1
    answer = counter
    print(answer)

# Functions

def divisible(n,x,y):
    """A simple function that takes an integer input n, and outputs if it is divisible by a range of x-y"""
    # Range of items to divide by
    divisors = list(range(x,y+1))
    # Double check of divisors
    # print(divisors)
    numbers = []
    for i in divisors:
        if n % i == 0:
            numbers.append(i)
    # If divisible by all the numbers return true
    if len(numbers) == len(divisors):
        return True
    else:
        return False

if __name__ == "__main__":
    main()