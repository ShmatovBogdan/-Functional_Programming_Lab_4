# Мін-макс нормалізація до [0,1]; якщо всі значення однакові — повернути нулі.

def minmax_scale(xs: list[float]) -> list[float]:
    min_x, max_x = min(xs), max(xs)
    if min_x == max_x:
        return [0.0 for _ in xs]
    return list(map(lambda x: (x - min_x) / (max_x - min_x), xs))

print(minmax_scale([10, 20, 30]))
print(minmax_scale([5, 5, 5]))
