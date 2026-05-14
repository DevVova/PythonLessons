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