# Sum of even values in Fibonacci Sequence up to an including 4 million
# Fibonacci Sequence
fibonacci_sequence = [1, 2]
while len(fibonacci_sequence) < 4000001:
    new_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(new_number)

# Get the even numbers
even_numbers = []
for i in fibonacci_sequence:
    if i % 2 == 0:
        even_numbers.append(i)

# Sum the even numbers
sum = sum(even_numbers)

print(sum)

