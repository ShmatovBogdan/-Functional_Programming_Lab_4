# Залишити лише «схожі на e-mail» рядки (дуже спрощено: містять @ і крапку після @).

from typing import Iterable

def filter_emails(items: Iterable[str]) -> list[str]:
    return list(filter(lambda s: "@" in s and "." in s.split("@")[-1], items))

emails = ["a@b.com", "wrong@", "x@y", "john.doe@mail.org"]
print(filter_emails(emails))  # ['a@b.com', 'john.doe@mail.org']
