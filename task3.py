# Написати валідатор: довжина ≥ 8, є велика літера, є мала, є цифра, є спецсимвол.

def is_strong_password(s: str) -> bool:
    return (
        len(s) >= 8
        and any(c.isupper() for c in s)
        and any(c.islower() for c in s)
        and any(c.isdigit() for c in s)
        and any(not c.isalnum() for c in s)
    )

print(is_strong_password("Qwerty12!"))
print(is_strong_password("1234"))
