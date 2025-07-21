# Лямбда-выражения в языке Python представляют небольшие анонимные функции,
# которые определяются с помощью оператора lambda.
fun = lambda a, b: a + b


def do_operation(a, b, op):
    result = op(a, b)
    print(result)


def select_function(choice):
    if choice == 1:
        return lambda a, b: a * b
    elif choice == 2:
        return lambda a, b: a / b
    else:
        return lambda a, b: a - b


do_operation(23, 12, lambda a, b: a - b)
do_operation(4, 5, fun)
do_operation(156, 78, select_function(22))
