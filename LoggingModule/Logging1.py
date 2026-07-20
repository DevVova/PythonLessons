import logging

"""
    Если написать filemode='a', то будет постоянно дописывать в лог, а если 'w', то заново с чистого листа.
    Для того чтобы писать в файл нужно написать filename="ThisFile.log" и он, если его нет, создастся.
    Если ничего не указать то будет режим 'a'. Если параметр filemode не указан, по умолчанию используется режим "a"
    (дозапись в конец файла).

    Записи в лог-файле имеют формат <logging-level>:<name-of-the-logger>:<message>. По умолчанию <name-of-the-logger>,
    имя логгера, установлено в root, так как мы пока не настраивали пользовательские логгеры.

    В logging для параметра format можно использовать довольно много полей объекта LogRecord.

    Самые популярные:

    Поле	Что выводит
    %(asctime)s	время создания записи
    %(levelname)s	название уровня (DEBUG, INFO...)
    %(levelno)s	числовой уровень (10, 20...)
    %(message)s	текст сообщения
    %(name)s	имя логгера
    %(filename)s	имя файла
    %(pathname)s	полный путь к файлу
    %(module)s	имя модуля без .py
    %(funcName)s	имя функции
    %(lineno)d	номер строки
    %(thread)d	ID потока
    %(threadName)s	имя потока
    %(process)d	ID процесса
    %(processName)s	имя процесса
    %(created)f	Unix-время создания записи
    %(msecs)d	миллисекунды
    %(relativeCreated)d	миллисекунды с запуска программы
"""
logging.basicConfig(
    level=logging.INFO,
    filename="ThisFile.log",
    filemode="a",
    format="%(asctime)s   %(name)s   %(levelname)s    %(message)s   line -> %(lineno)d   from module -> %(module)s",
)  #  Если так указать, то даже дебажные сообщения попадут в консоль на вывод, только без filename="ThisFile.log" иначе в консоле будет пусто.
logging.debug("This is a debug!")
logging.info("This is an info.")
logging.warning("This is a warning!!")
logging.error("This is an error!!!")
logging.critical("This is a critical message!!!")

# Ниже пример того, как можно добавлять пустую строку в конце файла при окончании.
f = open("ThisFile.log", "a", encoding="utf-8")
f.write("\n")
f.close()
