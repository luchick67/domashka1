def average_grade(a, b, c):
    return (a + b + c) / 3


def grade_message(x):
    if x >= 4.5:
        return "Отлично"
    elif x >= 3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"


# Проверка для оценок 5, 4, 5
s = average_grade(5, 4, 5)
m = grade_message(s)
print(f"Средний балл: {s:.2f} — {m}")

# Проверка для оценок 3, 4, 3
s = average_grade(3, 4, 3)
m = grade_message(s)
print(f"Средний балл: {s:.2f} — {m}")