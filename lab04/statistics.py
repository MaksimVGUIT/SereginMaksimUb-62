n = int(input("Введите количество чисел: "))

first = int(input("Введите число: "))
total = first
positive_count = 1 if first > 0 else 0
maximum = first

for _ in range(n - 1):
    x = int(input("Введите число: "))
    total += x

    if x > 0:
        positive_count += 1

    if x > maximum:
        maximum = x

print("Сумма:", total)
print("Количество положительных:",positive_count)
print("Максимум:",maximum)