# Function to find prime factors of a number
def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors

# Take user input for the number
try:
    num = int(input("Enter a number: "))
    if num < 2:
        print("Prime factorization is not possible for numbers less than 2.")
    else:
        factors = prime_factors(num)
        if len(factors) == 1 and factors[0] == num:
            print(f"{num} is a prime number.")
        else:
            print(f"The prime factors of {num} are: {factors}")
except ValueError:
    print("Please enter a valid integer.")
