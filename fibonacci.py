def fibonacci(n):
    """Return a list of the first n Fibonacci numbers, starting from 0."""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    for i, num in enumerate(fibonacci(100), start=1):
        print(f"{i}: {num}")
