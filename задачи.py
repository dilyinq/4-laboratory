def is_divisible_by_three(num):
    if num % 3 == 0:
        return True
    else:
        return False
num = int(input("Введите число: "))
if is_divisible_by_three (num):
    print("Число делится на 3")
else:
    print("Число не делится на 3")

def divide_numbers():
    try:
        user_input = float(input("Введите число: "))
        result = 100 / user_input
        print(f"Результат деления 100 на введенное число: {result}")
    except ValueError:
        print("Ошибка! Введите число, а не строку.")
    except ZeroDivisionError:
        print("Ошибка! Нельзя делить на ноль.")
divide_numbers()

def is_magic_date(date):
    day, month, year = date.split('.')
    day = int(day)
    month = int(month)
    year = int(year)
    a = day * month
    last_two_digits = str(year)[-2:]
    return a == int(last_two_digits)
date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if is_magic_date(date):
    print("Дата является магической")
else:
    print("Дата не является магической")

def is_lucky_ticket(ticket_number):
    if len(ticket_number) % 2 != 0:
        return False
    half_length = len(ticket_number) // 2
    first_half = list(ticket_number[:half_length])
    second_half = list(ticket_number[half_length:])
    if sum(map(int, first_half)) == sum(map(int, second_half)):
        return True
    else:
        return False
ticket_number = input("Введите число ")
if is_lucky_ticket(ticket_number):
    print("Это счастливый билет")
else:
    print("Это не счастливый билет")