def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = 5
factorial_result = factorial(n)

print(f"Factorial of {n} is: {factorial_result}")

print(f"\nStep by step calculation:")
print(f"5! = 5 × 4 × 3 × 2 × 1 = {factorial_result}")

