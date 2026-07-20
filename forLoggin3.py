import datetime
import locale
import logging

from utils.ForLogging import write_log_session_header

"""
Допустим  мы хотим писать логи так, чтобы каждый раз при запуске приложения 
в начале в файле шла дата и время начала ведения лога и она отделялась от
предыдущих логов пробелами. А в случае, если это самый первый лог, то не отделялась
пробелом, а вверху была запись даты и времени лога.
"""
# r значит raw string — «сырая строка». Без r обратный слеш \ начинает обозначать специальные символы.
# Если такой файл есть, то открываем его и в конце перевод строки делаем. Это потому что режим "a".
"""
Вот ниже примеры других режимов:
open("file.txt", "r")   # читать
open("file.txt", "w")   # перезаписать
open("file.txt", "a")   # дописать в конец
open("file.txt", "x")   # создать новый, если его нет
open("file.txt", "r+")  # читать и изменять
"""
LOG_FILE_NAME = "AppLogFile.log"
LOG_FILE_PATH = rf"C:\C\Python\MyPrograms\PythonLessons\{LOG_FILE_NAME}"
timeNow = datetime.datetime.now()

locale.setlocale(
    locale.LC_ALL, ""
)  # Используем локаль, для указания локального языка и прочего.

write_log_session_header(LOG_FILE_PATH, LOG_FILE_NAME, timeNow)

logging.basicConfig(level=logging.DEBUG, filename=LOG_FILE_PATH, encoding="utf-8")
logging.info("Это новая запись")
