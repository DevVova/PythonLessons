class Person:
    pass


class Person2:
    name = "Helen"
    age = 21


class Human:
    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age


class Car:
    def __init__(self, color):
        self.color = color
        print(f"Created class Car. Its color is {color}")

    def info(self):
        print(f"This is a car. It's {self.color}.")


class House:
    def __init__(self, price, address):
        self.price = price
        self.address = address
        print(f"Создан дом по адресу {address}.")

    # Ниже пример деструктора.
    # При завершении программы автоматически будет выполняться деструктор объекта.
    def __del__(self):
        print(f"Снесён дом по адресу {self.address}.")


# Ниже пример задокументированного класса.
class Friend:
    """
    Это класс под названием 'Friend'
    """

    def __init__(self, name, age):
        self.name = name
        """
        :param name: Этот атрибут хранит имя.
        """
        self.age = age
        print("Создан экземпляр класса 'Friend'.")


pasha = Friend("Pasha", 47)
print(pasha.name)

sam = Person()
sam.name = "Sam"
print(sam.name)

print()
my_house = House(230000, "5 Avenue")
