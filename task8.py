# Побудувати словник char -> count для рядка.

from functools import reduce

def char_hist(s: str) -> dict[str, int]:
    return reduce(lambda acc, c: acc | {c: acc.get(c, 0) + 1}, s, {})

print(char_hist("aba c")) # {'a': 2, 'b': 1, ' ': 1, 'c': 1}
