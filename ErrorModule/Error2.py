class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Недопустимое значение {self.value}!"


class House:
    def __init__(self, price):
        if price != 22:
            self.price = price
        else:
            raise MyError(price)

    def info(self):
        print(f"The house price is {self.price}.")


try:
    himHouse = House(40000)
    himHouse.info()

    myHouse = House(22)
    myHouse.info()
except Exception as e:
    print(e)
