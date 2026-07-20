myList1 = list()
anyList = [12, 34, 5, "Helen", True]
list1 = list(anyList)
print(list1[-1])
num1, num2, num3, name, usl = (
    list1  # Меньше чем в списке элементов указывать нельзя, иначе ошибка будет.
)
print(num3)

i = 0
while i < len(list1):
    print(f"{list1[i]}", end=" ")
    i += 1
print()
print(list1[:-2])  # Будет печатать до предпоследнего элемента не включительно.
print(
    list1[1:-1]
)  # Будет печатать со второго включительно до предпоследнего элемента не включительно.
print(list1[::2])  # Будет печатать все элементы с шагом 2.

list1.reverse()
print(list1)
