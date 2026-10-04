price = float(input("Введите цену 1 тетради: "))
if price <= 0:
    print("Ошибка: цена должна быть больше 0.")
    exit()
quantity = int(input("Введите количество тетрадей: "))
if quantity <= 0:
    print("Ошибка: количество должно быть больше 0.")
    exit()
total_cost = price * quantity
print(f"Стоимость покупки: {total_cost} руб.")
sum=float(input("Введите внесенные деньги: ")) 
change = sum - total_cost
print(f"Сдача: {change} руб.")