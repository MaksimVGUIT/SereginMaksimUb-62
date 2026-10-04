order = input("Введите № заказа: ")
cus=input("Введите имя заказчика: ")
item1 = input("Введите название напитка: ")
item1_qty = int(input("Введите количество напитков: "))
item1_price = float(input("Введите цену 1 напитка: "))
item2 = input("Введите название десерта: ")
item2_qty = int(input("Введите количество десертов: "))  
item2_price = float(input("Введите цену 1 десерта: "))
dilivery = float(input("Введите стоимость доставки: "))
sale = float(input("Введите % скидки: "))
sum=float(input("Введите внесенные деньги: "))

cost1 = item1_qty * item1_price
cost2 = item2_qty * item2_price
total_cost = cost1 + cost2 
global_cost = total_cost + dilivery
sale_amount = global_cost * (sale / 100)
global_cost_sale = global_cost - sale_amount
change = sum - global_cost

print("Заказ №:", order)
print("Имя заказчика:", cus)
print()
print("Название | Количество | Цена | Стоимость")
print(f"{item1} | {item1_qty} | {item1_price:.2f} | {cost1:.2f}")
print(f"{item2} | {item2_qty} | {item2_price:.2f} | {cost2:.2f}")
print()
print(f"Стоимость товаров без скидки: {total_cost:.2f} руб.")
print(f"Скидка: {sale:.2f}%")
print(f"Размер скидки: {sale_amount:.2f} руб.")
print(f"Стоимость товаров со скидкой: {global_cost_sale:.2f} руб.")
print("Стоимость доставки:", dilivery)
print("Общая стоимость заказа:", global_cost)
print("Общее количество товаров:", item1_qty + item2_qty)
print("Общая стоимость заказа со скидкой и доставкой:", global_cost_sale + dilivery)

print(f"Внесенные деньги: {sum:.2f} руб.")
if change < 0:
    print("Недостаточно средств для оплаты заказа.")
else:
    print(f"Сдача: {change:.2f} руб.")