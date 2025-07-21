def info(input_name, input_age):
    print(f"Hello {input_name}! You are {input_age} years old.")


# Ниже пример параметра со значением по умолчанию. Аргумент в эту функцию передавать не обязательно.
def say_hello(input_name="Vova"):
    print(f"Hello {input_name}!")


# Если функция имеет несколько параметров, то необязательные параметры должны идти после обязательных.
def new_info(input_name, input_age=18):
    print(f"He is {input_name}. He's {input_age} years old.")


# Передача значений параметрам по имени. Именованные параметры.
def info_of_car(model, price):
    print(f"This is a {model}. Its price is {price}.")


# Символ * позволяет установить, какие параметры будут именованными - то
# есть такие параметры, которым можно передать значения только по имени. Все
# параметры, которые располагаются справа от символа *, получают значения только по имени:
def full_info(human_age, *, first_name, last_name):
    print(f"Your first name is {first_name}. Your last name is {last_name}. You are {human_age} years old.")


# Если наоборот, надо определить параметры которым можно передавать значения
# только по позиции, то есть позиционные параметры, то можно использовать
# символ /: все параметры, которые идут до символа / , являются позиционными
# и могут получать значения только по позиции
def info_of_house(address, /, color, price):
    print(f"It's house is {color}. Its address is {address}. And its price is {price}.")


# Неопределенное количество параметров
def sum_num(*num):
    result = 0
    for n in num:
        result += n
    return result


# Пример использования return в качестве инструкции по выходу из функции.
def print_age(your_age):
    your_age = int(your_age)
    if 0 <= your_age < 140:
        print(f"You are {your_age} years old.")
        return
    if your_age <= 0 or your_age > 140:
        print_age(input("Введите ещё раз свой возраст, потому что предыдущий был не корректен: "))


name = input("Enter your name:\n")
age = input("Enter your age:\n")
info(name, age)

print()
say_hello()
say_hello("Kevin")

print()
new_info("Kolya", 45)

print()
info_of_car(price=20000, model="BMW")

print()
full_info(23, first_name="Tom", last_name="Hanks")

print()
info_of_house("25 Avenue", "Green", 45000000)

print()
print(sum_num(34, 22, 12, 90, 34))

print()
print_age(22)
print_age(150)
print_age(input("Введите свой возраст: "))