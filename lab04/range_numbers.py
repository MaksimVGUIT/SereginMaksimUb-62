a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a < b:
    for i in range(a, b + 1):
        print(i)
elif a > b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    print(a)