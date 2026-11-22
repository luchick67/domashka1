def summa_biletov(k, c=12):
    return k * c
def itogovaya_cena(k, s=False):
    t = summa_biletov(k)
    if s:
        return t * 0.75
    return t
a = itogovaya_cena(3)
print(f"3 обычных билета: {a:.0f} руб.")
b = itogovaya_cena(4, s=True)
print(f"4 билета для школьной группы: {b:.0f} руб.")
c = summa_biletov(2, c=15)
print(f"2 билета по 15 руб.: {c:.0f} руб.")