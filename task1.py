# Розробити декоратор log_calls, який друкує ім’я функції, аргументи/іменовані 
# aргументи та результат.

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}{args if args else ''}{kwargs if kwargs else ''}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} = {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(2, 3))
