import os
import datetime


# Docstring функции должен быть первой строкой внутри функции.
def write_log_session_header(log_file_path: str, log_file_name: str):
    """
    Функция добавляет в указанный лог заголовок с датой и временем начала новой сессии логирования.
    Args:
        log_file_path (str): Полный путь к файлу журнала.
        file_name (str): Имя файла журнала.
        timeNow(datetime): Момент времени.
    """

    timeNow = datetime.datetime.now()
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
