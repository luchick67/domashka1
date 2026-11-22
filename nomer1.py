def sredniy_ball(a, b, c):
    return (a + b + c) / 3
def tekst_ocenki(x):
    if x >= 4.5:
        return "Отлично"
    elif x >= 3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"
s = sredniy_ball(5, 4, 5)
m = tekst_ocenki(s)
print(round(s, 2), m)
s = sredniy_ball(3, 4, 3)
m = tekst_ocenki(s)
print(round(s, 2), m)