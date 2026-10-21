text = input("Введите целые числа через пробел: ")
numbers = []
for part in text.split():
    numbers.append(int(part))
transformed = numbers.copy()
for i in range(len(transformed)):
    if transformed[i] < 0:
        transformed[i] = abs(transformed[i])

print("Исходный список:", numbers)
print("Новый список:", transformed)