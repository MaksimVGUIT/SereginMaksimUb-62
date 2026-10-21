text = input("Введите текст: ")
cleaned = text.replace(" ", "").lower()
if cleaned == "":
    print("Нет текста")
else:
    is_palindrome = True

    for i in range(len(cleaned) // 2):
        if cleaned[i] != cleaned[-1 - i]:
            is_palindrome = False
            break

    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")