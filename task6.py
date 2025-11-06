# Для кожного елемента x обчислити scale * x + shift.

from typing import Iterable

def scale_and_shift(xs: Iterable[float], scale: float, shift: float) -> list[float]:
    return list(map(lambda x: scale * x + shift, xs))

print(scale_and_shift([1, 2, 3], 2.0, -1.0))  # [1.0, 3.0, 5.0]
