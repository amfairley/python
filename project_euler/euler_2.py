# Sum of even values in Fibonacci Sequence up to an including 4 million
import numpy as np

def main():
    # Fibonacci Sequence
    fibonacci_sequence = np.array([1,2])
    while fibonacci_sequence.size < 4000001:
        new_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence = np.append(fibonacci_sequence, new_number)

    # Get the even numbers
    evens = np.array([])
    for i in fibonacci_sequence:
            if i % 2 == 0:
                evens = np.append(evens, i)

    # Sum the even numbers

    sum = np.sum(evens)
    print(sum)

if __name__ == "__main__":
     main()






