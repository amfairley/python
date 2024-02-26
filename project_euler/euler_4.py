# Find the largest palindrome made from the product of two 3-digit numbers
def main():
    palindromes = []
    for i in range(0,999):
        for j in range(0,999):
            product = i * j
            # Convert the answer to a string
            product = str(product)
            if product not in palindromes:
                if len(product) < 6:
                    continue
                # elif ((len(product) == 2) or (len(product) == 3)) & (product[0] == product [-1]):
                #     palindromes.append(product)
                # elif (len(product) == 4 or len(product) == 5) & (product[0] == product [-1]) & (product[1] == product [-2]):
                #     palindromes.append(product)
                elif (len(product) == 6) & (product[0] == product [-1]) & (product[1] == product [-2]) & (product[2] == product[3]):
                    palindromes.append(int(product))

    print(max(palindromes))

if __name__ == "__main__":
    main()