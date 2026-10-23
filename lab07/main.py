from functions import (
    average,
    is_palindrome,
    normalize_text,
    select_numbers,
    sum_digits,
)


def read_numbers(line):
    return [int(part) for part in line.split()]

def main():
    try:
        number = int(input("Целое число: "))
        print("Сумма цифр:", sum_digits(number))

        numbers = read_numbers(input("Числа через пробел: "))
        avg = average(numbers)
        if avg is None:
            print("Нет данных")
        else:
            print("Среднее:", avg)

        text = input("Произвольный текст: ")
        print("Нормализованный текст:", repr(normalize_text(text)))
        print("Палиндром:", is_palindrome(text))

        threshold = int(input("Порог (целое неотрицательное): "))
        if threshold < 0:
            print("Порог не может быть отрицательным")
            return
        print("Числа с модулем больше порога:", select_numbers(numbers, threshold))
    except ValueError:
        print("Ошибка: введено не целое число")


if __name__ == "__main__":
    main()