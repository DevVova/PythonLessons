# В Python функция фактически представляет отдельный тип. Так мы можем
# присвоить переменной какую-нибудь функцию и затем, используя переменную,
# вызывать данную функцию.
def print_hello():
    print("Hello!")


def sum1(a, b):
    return a + b


def multiply(a, b):
    return a * b


# Функция как параметр функции
def operation_any(a, b, op):
    return op(a, b)


# Функция как результат функции
def select_operation(choice):
    if choice == 1:
        return sum1
    else:
        return multiply


my_hello = print_hello
my_hello()

print()
operation = sum1
result = operation(24, 2)
print(result)
operation = multiply
print(operation(24, 24))

print()
print(operation_any(17, 17, multiply))

print()
my_operation = select_operation(34)
print(my_operation(34, 34))
operation = select_operation(1)
print(operation(1, 1))
operation = select_operation(11)
result = operation
print(result(23, 23))
