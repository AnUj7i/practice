def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def are_twin_primes(a, b):
    if abs(a - b) == 2 and is_prime(a) and is_prime(b):
        return True
    return False

# Example usage
num1 = 111
num2 = 13

if are_twin_primes(num1, num2):
    print(f"{num1} and {num2} are twin primes.")
else:
    print(f"{num1} and {num2} are not twin primes.")
