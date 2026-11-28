def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

assert factorial(0) == 1
assert factorial(5) == 120


def factorial_iterative(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


print("Трассировка factorial(3):")
print("  вызовы:   factorial(3) -> factorial(2) -> factorial(1) -> factorial(0)")
print("  возвраты: 1 -> 1 -> 2 -> 6")


print("\nСравнение рекурсивной и итеративной версий:")
for n in range(0, 21):
    a=factorial(n)
    b=factorial_iterative(n)
    assert a == b, f"Расхождение при n={n}: {a} !={b}"
    print(f"{n:>2}!={a}")
print("\nВсе значения для 0..20 совпали")