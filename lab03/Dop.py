year = int(input("Введите год: "))
if year < 1 or year > 9999:
    print("Ошибка диапазона")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Год високосный")
else:
    print("Год не високосный")