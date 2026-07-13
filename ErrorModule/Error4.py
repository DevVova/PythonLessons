# Пример генерации исключения.
try:
    num = int(input("Введите число от 1 до 100: "))
    if num < 1 or num > 100:
        raise Exception("Число не входит в диапазон от 1 до 100.")
    print(f"Вы ввели число - {num}")
except ValueError:
    print("Вы ввели не число.")
except Exception as e:
    print(e)


# Пример создания своего исключения.
class LotIsFloat(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Недопустимое значение для лота!"


class MyLot:
    def __init__(self, value):
        # isinstance() — это встроенная функция Python, которая проверяет, является ли объект экземпляром указанного класса (типа).
        if isinstance(value, int):
            self.value = value
        else:
            raise LotIsFloat(value)

    def info(self):
        print(f"Lot is {self.value}.")


try:
    lot1 = MyLot(5)
    lot1.info()

    lot2 = MyLot(0.23)
    lot2.info()
except Exception as e:
    print(e)
