subject1 = input("Введите первый предмет: ")
lesson1 = int(input("Введите количество МИНУТ подготовки по первому предмету в неделю: "))
duration1 = int(input("Введите количество недель подготовки по первому предмету: "))

if lesson1 <0:
    print("Ошибка: количество минут не может быть отрицательным.")
elif duration1 <=0:
        print("Ошибка: количество недель не может быть отрицательным.")
else:
    subject2 = input("Введите второй предмет: ")
    lesson2 = int(input("Введите количество минут подготовки по второму предмету в неделю: "))
    duration2 = int(input("Введите количество недель подготовки по второму предмету: "))
    if lesson2 <0:
        print("Ошибка: количество минут не может быть отрицательным.")
    elif duration2 <=0:
        print("Ошибка: количество недель не может быть отрицательным.")
    else:
         time_available = float(input("Введите количество часов, доступных для подготовки в неделю: "))
    load1 = lesson1 * duration1
    load2 = lesson2 * duration2
    total_minutes = load1 + load2
    total_hours = total_minutes / 60
    free_hours = time_available - total_hours
    four_weeks= total_hours * 4
    if time_available < total_hours:
            print("Недостаточно времени для подготовки по обоим предметам.")
    else: 
         print ()
         print("Учебная нагрузка по предметам:")
         print(f"{subject1}: {load1} минут")
         print(f"{subject2}: {load2} минут")
         print(f"Общее количество минут подготовки: {total_minutes} минут")
         print(f"Общая учебная нагрузка: {total_hours:.2f} часов")
print(f"Свободное время: {free_hours:.2f} часов")
print(f"Учебная нагрузка за 4 недели: {four_weeks:.2f} часов")