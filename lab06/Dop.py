text = input("Введите целые числа через пробел: ")
numbers = []
for part in text.split():
    numbers.append(int(part))
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print("Исходный список:", numbers)
print("Без повторов:", unique)