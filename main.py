from datetime import datetime
import time
import locale


timestampNow = time.time()
print(timestampNow)
datetimeNow = datetime.fromtimestamp(timestampNow)
locale.setlocale(category=locale.LC_TIME, locale="")
print(f"Сегодня - {datetimeNow.strftime("%d число %y года. А день недели - %A")}")
print(f"А если перевести обратно в timestamp - {datetimeNow.timestamp()}")