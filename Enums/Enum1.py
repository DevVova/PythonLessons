from enum import Enum, auto


# Каждому элементу перечисления должно быть установленно значение(число или строка), либо auto(), если значение не важно.
class Broker(Enum):
    FINAM = auto()
    BYBIT = auto()
    IB = auto()

class Country(Enum):
    USA = 'USA'
    RUSSIA = "Russia"

class Auto(Enum):
    BMW = 23000
    AUDI = 12000

myBroker = Broker.FINAM
print(myBroker.name)

myCountry = Country.USA
print(f"My country is {myCountry.value}!")

myAuto = Auto.BMW
priceAuto = myAuto.value
print(priceAuto)