# Функции

# Задание 1
# 1.Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра,
# приводит их к строке и отдает объединенными через разделитель delimiter
# 2.Вызовите функцию, передав в нее два аргумента "Learn" и "python",
# положите результат в переменную и выведите ее значение на экран
# 3.Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&'):
    strin = f'{one} {delimiter} {two}'
    return strin


perem = get_summ('Learn', 'python')
print(perem.upper())


# Задание 2
# Создайте в редакторе файл price.py
# Создайте функцию format_price, которая принимает один аргумент price
# Приведите price к целому числу (тип int)
# Верните строку "Цена: ЧИСЛО руб."
# Вызовите функцию, передав на вход 56.24 и положите результат в переменную
# Выведите значение переменной с результатом на экран

def format_price(price):
    price = int(price)
    result = f'Цена: {price} руб.'
    return result


variable = format_price(56.24)
print(variable)