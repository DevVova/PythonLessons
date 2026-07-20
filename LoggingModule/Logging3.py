import os
import datetime
import locale
import logging

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

# Ниже блок кода для создания записи даты и времени логирования, с установкой пробела для лучшего чтения(читабельности).
# Я его выведу в отдельную функцию.
if os.path.exists(LOG_FILE_PATH):
    thisFile = open(LOG_FILE_NAME, "a", encoding="utf-8")
    thisFile.write(
        f"\n================{timeNow.strftime("%d.%m.%y(%A) %H:%M:%S:%f")}================\n"
    )
    thisFile.close()
else:
    thisFile = open(LOG_FILE_NAME, "a", encoding="utf-8")
    thisFile.write(
        f"================{timeNow.strftime("%d.%m.%y(%A) %H:%M:%S:%f")}================\n"
    )
    thisFile.close()

logging.basicConfig(level=logging.DEBUG, filename=LOG_FILE_PATH, encoding="utf-8")
logging.info("Это новая запись")


# Docstring функции должен быть первой строкой внутри функции.
def write_log_session_header(log_file_path: str, log_file_name: str):
    """
    Функция добавляет в лог заголовок с датой и временем начала новой сессии логирования.
    Args:
        log_file_path (str): Полный путь к файлу журнала.
        file_name (str): Имя файла журнала.
    """

    if os.path.exists(log_file_path):
        thisFile = open(log_file_name, "a", encoding="utf-8")
        thisFile.write(
            f"\n================{timeNow.strftime("%d.%m.%y(%A) %H:%M:%S:%f")}================\n"
        )
        thisFile.close()
    else:
        thisFile = open(log_file_name, "a", encoding="utf-8")
        thisFile.write(
            f"================{timeNow.strftime("%d.%m.%y(%A) %H:%M:%S:%f")}================\n"
        )
        thisFile.close()
