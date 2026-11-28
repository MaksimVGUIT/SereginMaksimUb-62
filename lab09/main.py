from table import row_sums, column_sums, diagonal_pattern, transform
def main():
    print("=== Ввод таблицы ===")

    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))

    while rows <= 0 or columns <= 0:
        print("Количество строк и столбцов должно быть положительным.")
        rows = int(input("Количество строк: "))
        columns = int(input("Количество столбцов: "))

    matrix = []

    for i in range(rows):
        row = [int(part) for part in input(
            f"Введите {columns} числа для строки {i + 1}: "
        ).split()]

        while len(row) != columns:
            print(f"Нужно ввести ровно {columns} чисел.")
            row = [int(part) for part in input(
                f"Повторите строку {i + 1}: "
            ).split()]

        matrix.append(row)

    print("\nИсходная таблица:")
    for row in matrix:
        print(*row)

    print("\nСуммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    print("\n=== Преобразование (вариант 3) ===")
    new_matrix = transform(matrix)

    print("Исходная таблица:")
    for row in matrix:
        print(*row)

    print("Преобразованная таблица:")
    for row in new_matrix:
        print(*row)

    print("\n=== Диагональный узор ===")
    size = int(input("Введите положительный размер узора: "))

    while size <= 0:
        print("Размер должен быть положительным.")
        size = int(input("Повторите размер: "))

    pattern = diagonal_pattern(size)

    for row in pattern:
        print(*row)


if __name__ == "__main__":
    main()