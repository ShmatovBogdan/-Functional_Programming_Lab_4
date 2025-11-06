# Повернути імена топ-K студентів за спаданням score. За рівності — за ім’ям зростаюче.

def top_k(students: list[dict[str, int | str]], k: int) -> list[str]:
    sorted_students = sorted(students, key=lambda s: (-s["score"], s["name"]))
    return [s["name"] for s in sorted_students[:k]]

students = [
    {"name": "Ann", "score": 90},
    {"name": "Bob", "score": 95},
    {"name": "Ada", "score": 95}
]

print(top_k(students, 2))  # ['Ada', 'Bob']
