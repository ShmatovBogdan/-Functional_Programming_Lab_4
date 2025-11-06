# Перевір наявність принаймні одного простого числа.

from typing import Iterable

def has_prime(nums: Iterable[int]) -> bool:
    is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    return any(is_prime(n) for n in nums)

print(has_prime([4, 6, 8, 9]))
print(has_prime([4, 6, 7, 9, 10]))
