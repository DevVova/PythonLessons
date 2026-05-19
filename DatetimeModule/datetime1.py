import datetime

"""
Модуль предназначен для работы с датой и временем.
"""
today = datetime.date(2026, 5, 14)
print(today)

                                           # Класс date.

# Пример получения даты, которая сегодня:
today = datetime.date.today()
print(today)
todayMonth = datetime.date.today().month  # Если необходимо получить месяц, который сейчас.
print(todayMonth)

yesterday = datetime.date(2026, 5, datetime.date.today().day - 1)  # Вот так можно получить вчерашнюю дату.
print(yesterday)
print("{}.{}.{}".format(yesterday.day, yesterday.month, yesterday.year))

                                           # Класс datetime.
                                           
time_now = datetime.datetime.now().minute  # Вот так можно узнать какая сейчас минута.
print(time_now)
time = datetime.datetime.now()  # А вот так полностью время и дату сейчас можно узнать.
print(time)

day = datetime.datetime(2026, 5, 18)
print(day)
print("{}.{}.{} - my birth day.".format(day.day, day.month, day.year))

                                          # # Класс time.
t = datetime.datetime.now().time().hour  # Вот как можно узнать который сейчас час.
print(t)

# Преобразование из строки в дату.


# Для определения формата мы можем использовать следующие коды:

# %d: день месяца в виде числа

# %m: порядковый номер месяца

# %y: год в виде 2-х чисел

# %Y: год в виде 4-х чисел

# %H: час в 24-х часовом формате

# %M: минута

# %S: секунда

deadLine = datetime.datetime.strptime("19/05/2026 20:00", "%d/%m/%Y %H:%M")
print(deadLine)