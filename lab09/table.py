def row_sums(matrix):
    sums = []
    for row in matrix:
        sums.append(sum(row))

    return sums
def column_sums(matrix):
    if not matrix:
        return []
    columns = len(matrix[0])
    sums = []

    for column in range(columns):
        total = 0

        for row in matrix:
            total += row[column]

        sums.append(total)

    return sums


def diagonal_pattern(size):
    matrix = []

    for row in range(size):
        current_row = []

        for column in range(size):
            if row == column:
                current_row.append(0)
            elif row < column:
                current_row.append(1)
            else:
                current_row.append(2)

        matrix.append(current_row)

    return matrix


def transform(matrix):
    result = []

    for row in matrix:
        new_row = []

        for number in row:
            if number % 2 == 0:
                new_row.append(number * 2)
            else:
                new_row.append(number)

        result.append(new_row)

    return result