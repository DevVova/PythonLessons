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


# Можно вместо Exception указать конкретную ошибку MyError.
# Если указать himHouse = House(40000) после myHouse = House(22), то оно будет игнорировано, так как после пойманной ошибки перейдёт в блок except.
try:
    himHouse = House(40000)
    himHouse.info()

    myHouse = House(22)
    myHouse.info()
except Exception as e:
    print(e)
