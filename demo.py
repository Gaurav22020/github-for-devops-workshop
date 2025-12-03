import math
def is_prime(n):
    # Numbers less than 2 are not prime
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    # Check for factors from 3 up to the square root of n, skipping even numbers
    # The step is 2, so we only check odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    # If no factors are found, the number is prime
    return True
# Example usage:
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
