text = input("Введите целые числа через пробел: ")
numbers = []
for part in text.split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    print("Количество:", len(numbers))
    print("Сумма:", sum(numbers))
    print("Минимум:", min(numbers))
    print("Максимум:", max(numbers))
    print("Среднее:", f"{sum(numbers) / len(numbers):.2f}")