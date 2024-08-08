def fibonacci(n):
    if n < 0:
        return 'Argument n should not be negative, please try again.'
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # 5
print(fibonacci(12)) # 144
print(fibonacci(20)) # 6765
