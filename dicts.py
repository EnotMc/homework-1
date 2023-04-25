# Словари

# Задание 1
# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

dicts = {'city': 'Москва', 'temperature': '20'}
print(dicts['city'])
dicts['temperature'] = str(int(dicts['temperature'])-5)
print(dicts)


# Задание 2
# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря
# Выведите на экран весь словарь

print(dicts.get('country'))
dicts['country'] = 'Россия'
dicts['date'] = "27.05.2019"
print(len(dicts))
print(dicts)
