from typing import Dict

cache: Dict[int, int] = {}


def fib(n):
    # The base cases
    if n <= 1:  # First number in the sequence
        return 0
    elif n == 2:  # Second number in the sequence
        return 1
    else:
        # Check if we have already cached the result
        if n in cache:
            return cache[n]
        else:
            # Otherwise, calculate the result and cache it
            result = fib(n - 1) + fib(n - 2)
            cache[n] = result
            return result


print(fib(137))
