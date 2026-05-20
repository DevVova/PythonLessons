import datetime


now = datetime.datetime.now()
print(f"Сегодня {now.day} число, а месяц - {now.month}.")
yesterday = now - datetime.timedelta(days=1)
print(f"Вчера было {yesterday.day} число.")

print("===================")
deadLine = datetime.datetime.strptime("20/05/2026 10:55", "%d/%m/%Y %H:%M")
print(deadLine)
left = deadLine - now
print(f"Осталось {left} до конца")