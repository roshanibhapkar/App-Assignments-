# Fibonacci using Cache

def fibonacci(n, cache=None):
    if cache is None:
        cache = {}

    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)

    return cache[n]


# Input
n = int(input("Enter n: "))

print("Fibonacci number:", fibonacci(n))