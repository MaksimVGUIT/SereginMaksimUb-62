from functions import (
    average,
    is_palindrome,
    normalize_text,
    select_numbers,
    sum_digits,
)

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# --- Вариант 3: модуль больше порога ---
# контрольный пример
assert select_numbers([-5, 0, 2, 5], 2) == [-5, 5]
# пустой список
assert select_numbers([], 2) == []
# пустая выборка при непустом списке (совпадений нет)
assert select_numbers([-2, -1, 0, 1, 2], 2) == []
# граница: |x| == порог не входит, рядом с границей входит
assert select_numbers([-3, -2, 2, 3], 2) == [-3, 3]
# порог 0: подходят все, кроме нуля
assert select_numbers([0, -1, 1], 0) == [-1, 1]
# повторы сохраняются, порядок сохраняется
assert select_numbers([3, -4, 3, 1, -4], 2) == [3, -4, 3, -4]
# исходный список не изменяется
original = [-5, 0, 2, 5, 5]
backup = original.copy()
result = select_numbers(original, 2)
assert original == backup
assert result is not original

# --- Дополнительно: is_palindrome ---
assert is_palindrome("Топот") is True
assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("Привет") is False
assert is_palindrome("") is False
assert is_palindrome("   ") is False
assert is_palindrome("!!!") is False

# дробное среднее
assert abs(average([1, 2]) - 1.5) < 1e-9

print("Базовые проверки пройдены")