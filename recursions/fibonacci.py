cache = [None]*100

def fibonacci(n):
    if n < 0:
        return 'Argument should not be negative, please try again.'
    elif n <= 1:
        return n
    
    if not cache[n]:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

print(fibonacci(5))  # 5
print(fibonacci(12)) # 144
print(fibonacci(20)) # 6765
