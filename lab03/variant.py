value = int(input("Введите процент выполнения учебного плана: "))
if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 39:
    print("Начало")
elif value <= 99:
    print("В процессе")
else:
    print("Завершено")