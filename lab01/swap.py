first_room = input("Введите № первой аудитории: ")
second_room = input("Введите № второй аудитории: ")
print("Номера аудиторий до обмена ")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")
temp = first_room
first_room = second_room
second_room = temp
print("Номера аудиторий после обмена ")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")