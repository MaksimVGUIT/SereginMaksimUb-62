text = input("Введите целые числа через пробел: ")
numbers = []
for part in text.split():
    numbers.append(int(part))
selected = []
for number in numbers:
    if abs(number) > 5:
        selected.append(number)

sorted_numbers = sorted(selected)
print("Выбранные числа:", selected)
print("Количество:", len(selected))
print("Сумма:", sum(selected))
print("Отсортированная копия:", sorted_numbers)