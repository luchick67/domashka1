def analiz_ballov(*b):
    if len(b) == 0:
        return 0, 0, 0
    s = sum(b)
    k = len(b)
    m = s / k
    return s, k, m
def pechat_otcheta(n, **i):
    print(f"Команда: {n}")
    for k, v in i.items():
        print(f"- {k}: {v}")
s, k, m = analiz_ballov(8, 10, 7, 9)
print(f"Сумма: {s}, Количество: {k}, Среднее: {m}")
s, k, m = analiz_ballov(5, 5)
print(f"Сумма: {s}, Количество: {k}, Среднее: {m}")
s, k, m = analiz_ballov()
print(f"Сумма: {s}, Количество: {k}, Среднее: {m}")
print()
pechat_otcheta("Комета", trener="Иванов", gorod="Минск")