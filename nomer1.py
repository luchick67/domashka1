def average_grade(a, b, c):
    return (a + b + c) / 3
def grade_message(average):
    if average >= 4.5:
        return "Отлично"
    elif average >= 3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"
s = average_grade(5, 4, 5)
m = grade_message(s)
print(round(s, 2), m)
s = average_grade(3, 4, 3)
m = grade_message(s)
print(round(s, 2), m)