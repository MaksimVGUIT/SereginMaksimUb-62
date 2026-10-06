first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first <= second and first <= third:
    minimum = first
elif second <= first and second <= third:
    minimum = second
else:
    minimum = third
print(f"Минимальное число: {minimum}")