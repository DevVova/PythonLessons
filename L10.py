# Вывод на консоль
# Например, мы хотим, чтобы все значения выводились на одной строке.
print("Hello", end = " ")
print("Vova", end = ". How ")
print("are you?")

# Консольный ввод
firstName = input("Input your first name: ")
lastName = input("Input your last name: ")
print("Your fullname", end = " is ")
print(f'{firstName} {lastName}.')