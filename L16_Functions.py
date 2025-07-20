def fun1():
    print("Hello!")


def fun2(a, b):
    return a + b


def fun3():
    def fun4():
        print("Это вызов локальной функции.")

    fun4()


def main():
    fun1()
    print(fun2(23, 44))
    fun3()


main()
