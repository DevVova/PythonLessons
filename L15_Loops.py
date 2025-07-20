num = 1
while num < 8:
    print(f"num = {num}", end=" ")
    num += 1
# Ниже блок на случай когда условие цикла не выполняется.
else:
    print(f"\nnum = {num} и поэтому цикл завершён.")
print()
print("Работа программы завершена.")

for x in range(3, 29, 4):
    print(x, end=" ")
else:
    print()  # Это я по факту после того как x вышла из range делаю перевод на новую строку.

    # А вот пример цикла в цикле:
for a in range(1, 10):
    for b in range(1, 10):
        print(f"{a * b}", end=" ")
    else:
        print()
else:
    print()

    # break and continue.
num1 = 1
while num1 < 16:
    if num1 == 3:
        num1 += 1
        continue  # оператор continue выполняет переход к следующей итерации цикла без его завершения
    if num1 == 8:
        break  # выходим из цикла
    print(num1, end = " ")
    num1 += 1
# Ниже код не выполнится.
else:
    print("Работа цикла завершена.")
