# Пример условных выражений.
a = 34
b = 7
print(a < b)
# Пример составных условных выражений.
c = 8
print((a > b and c > b) or a == b)
print(a > b or c < b)
print(not b > a)

# Оператор in возвращает True если в некотором наборе значений есть определенное значение.
my_range = range(1, 35)
print(a in my_range)

# Условные конструкции
if a < b:
    print("a < b")
elif a == b:
    print("a < b")
else:
    print("a > b")

# Условные конструкции вложенные
if a > b:
    if a == 34:
        print("a == 34")
else:
    print("a не больше b")
