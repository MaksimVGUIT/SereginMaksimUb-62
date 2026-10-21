text = input("Введите целые числа через пробел: ")
numbers = []
for part in text.split():
    numbers.append(int(part))
if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []

    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)

    print("Максимум:", maximum)
    print("Индексы максимума:", positions)