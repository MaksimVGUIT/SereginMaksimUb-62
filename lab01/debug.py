print("Фрагмент А")
first = "2"
second = "3"
print(f"Были строки, которые выводили значения переменных: {first} и {second}, если сделаем из них целые числа и сложим, то получим: {first + second}")
print(f"Ожидаемый результат: 5")
print(f"Тип first до преобразования: {type(first)}")
print(f"Тип second до преобразования: {type(second)}")
first = int(first)
second = int(second)
print(f"Тип first после преобразования: {type(first)}")
print(f"Тип second после преобразования: {type(second)}")
result = first + second
print(f"Результат сложения: {result}")

print()
print("Фрагмент Б")
age = input("Введите возраст: ")
print(f"Причина ошибки инпут возврашает строку, к строке нельзя прибавить число:")
print(f"Ожидаемый результат: при вводе 17, должно быть выведено 18")
print(f"Тип age до преобразования: {type(age)}")   
age = int(age)
print(f"Тип age после преобразования: {type(age)}")
result = age + 1
print(f"Возраст + 1: {result}")

print()
print("Фрагмент В")
first = 4
second = 7
third = 10
print(f"Без скобок сначала выполняется деление, потом сложение, поэтому результат будет: {first + second + third / 3} если добавим скобки то результат будет: {(first + second + third) / 3}")
print(f"Ожидаемый результат: 7.0")
average = (first + second + third) / 3
print(f"Результат после исправления: {average}")