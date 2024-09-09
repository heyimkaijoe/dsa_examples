def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('integer should be non-negative')
    elif n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 5! == 120
print(factorial(1))  # 1! == 1
print(factorial(0))  # 0! == 1
print(factorial(-1)) # ValueError
