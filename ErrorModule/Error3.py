# Пример практического задания, для преобразования строковых элементов списка одного в числовые элементы другого.
list1 = ["34", "5y", "2", "abc", "88", "u5"]
list2 = []

for i in list1:
    try:
        num = int(i)
        list2.append(num)
    except Exception as e:
        print(e)

for i in list2:
    print(i, end=" ")

print()

try:
    f = open("file.txt")
    print(f.read())
    f.close()
except FileNotFoundError as e:
    print(e)
