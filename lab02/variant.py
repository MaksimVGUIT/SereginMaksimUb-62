total = int(input("Введите количество фотографий: "))
capacity = int(input("Введите количество фотографий на одной странице: "))
pages = total // capacity
remainder = total % capacity
total_pages = (total + capacity - 1) // capacity
print(f"Полностью заполненных страниц: {pages}")
print(f"Осталось фотографий: {remainder}")
print(f"Всего нужно страниц: {total_pages}")