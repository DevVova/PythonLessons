import datetime
import time


# Ниже пример как получить разницу в секундах между заданной датой и временем и тем что сейчас.
# Также можно получить дни и микросекунды.
# Также в примере продемонстрировано то, что даты можно сравнивать, но не объекты типа time и date. Только datetime.
time1 = datetime.datetime(2026, 5, 20, 23, 2, 30)
print(time1)
timeNow = datetime.datetime.now()
if time1 > timeNow:
    print("time1 > timeNow")
    print(time1 - timeNow)
    d = (time1 - timeNow).seconds
    print(f"Разница {d} секунд.")
elif time1 < timeNow:
    print("time1 < timeNow")
    print(timeNow - time1)
    d = (timeNow - time1).seconds
    print(f"Разница {d} секунд.")
else:
    print("time1 = timeNow")


# timestamp
# Timestamp — это метка времени, то есть число, которое показывает конкретный момент времени.
# Чаще всего timestamp хранит количество секунд или миллисекунд, прошедших с: 1 января 1970 года 00:00:00 UTC. Это называется Unix Epoch.

# Вот как получить метку времени, которая сейчас.
print(f"Сейчас метка времени равна - {time.time()}")

# Пример того как перевести метку времени в дату.
date3 = datetime.datetime.fromtimestamp(time.time())
print(date3)
# Перевести дату в timestamp обратно.
print(date3.timestamp())