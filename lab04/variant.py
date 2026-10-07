n = int(input("Введите количество чисел: "))

count = 0
total = 0

for _ in range(n):
    x = int(input("Введите число: "))

    if 10 <= x <= 20:
        count += 1
        total += x

print("Количество:",count)
print("Сумма:",total)
