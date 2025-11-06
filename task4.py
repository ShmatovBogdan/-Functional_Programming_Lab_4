# Перевірити, що всі елементи відрізняються від першого не більше ніж на tol.

from typing import Iterable

def all_close(xs: Iterable[float], tol: float = 1e-6) -> bool:
    xs = list(xs)
    return all(abs(x - xs[0]) <= tol for x in xs)

print(all_close([1.0, 1.0000005, 0.9999999], tol=1e-5))
print(all_close([1.0, 1.1], tol=1e-3))
