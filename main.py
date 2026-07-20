class ForbiddenNumber(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Вы ввели запрещённое число - {self.value}."


class MyNumber:
    def __init__(self, number):
        if number == 99:
            raise ForbiddenNumber(number)
        else:
            self.number = number


try:
    num1 = int(input("Введите первое число, кроме 99: "))
    number1 = MyNumber(num1)
    num2 = int(input("Введите второе число, кроме 99: "))
    number2 = MyNumber(num2)
    res = number1.number / number2.number
    print(f"Результат деления равен -> {res}!")
except ZeroDivisionError:
    print("На ноль делить нельзя!!! А вы ввели второе число равное нулю!!!")
except ValueError:
    print("Вы ввели не число!!!")
except ForbiddenNumber as f:
    print(f)
except Exception as e:
    print(e)
