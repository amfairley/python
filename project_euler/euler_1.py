# Find the sum of the multiples of 3 or 5 below 1000
def main():

    # Make an empty list
    numbers = []

    # Add all multiples of 3 to the list
    for i in range(0,1000,3):
        numbers.append(i)

    # Add all multiples of 5 that are already not in the list
    for i in range(0,1000,5):
        if i not in numbers:
            numbers.append(i)
        else:
            continue

    # Sum all the numbers
    answer = sum(numbers)
    print(answer)

if __name__ == "__main__":
    main()