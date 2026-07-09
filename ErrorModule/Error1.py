import logging

logging.basicConfig(
    level=logging.INFO,
    filename="Error.log",
    encoding="utf-8",
    format="%(asctime)s %(message)s",
)  # encoding="utf-8", если не написать, то будут кракозярбы.
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    res = number1 / number2
    logging.info(f"Результат деления этих чисел - {res}.")
except ValueError:
    logging.error("Вы ввели не число.")
except (ZeroDivisionError, TypeError) as z:
    logging.error(
        f"Второе число 0, а на 0 делить нельзя. {z}"
    )  # С помощью as мы можем передать всю информацию об ошибке в переменную z.
except BaseException as e:
    logging.error(f"Ошибка, попробуйте ещё раз. Ошибка - {e}")
finally:
    f = open("Error.log", "a", encoding="utf-8")
    f.write("\n")
    f.close()
