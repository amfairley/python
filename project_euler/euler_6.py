# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def main(): 
    # Sum of first 100
    first_hundred = []
    for i in range(1,101):
        first_hundred.append(i)
    sum_first_hundred = sum(first_hundred)

    # Square the sum
    sum_square = sum_first_hundred * sum_first_hundred

    # First 100 squares
    hundred_squares = []
    for i in range(1,101):
        hundred_squares.append(i*i)

    # Sum of squares
    sum_of_squares = sum(hundred_squares)

    # Difference
    answer = sum_square -  sum_of_squares
    print(answer)

if __name__ == "__main__":
    main()