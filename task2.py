# Декоратор timeit міряє та друкує час виконання функції в мс.

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {(time.time() - start)*1000:.0f} ms")
        return result
    return wrapper

@timeit
def slow(n: int) -> int:
    time.sleep(0.05)
    return n * n

print(slow(10))
