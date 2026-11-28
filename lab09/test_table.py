from table import row_sums, column_sums, diagonal_pattern, transform

matrix = [[1, 2, 3], [4, 5, 6]]

assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]


matrix = [[1], [-1], [0]]

assert row_sums(matrix) == [1, -1, 0]
assert column_sums(matrix) == [0]

assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []


assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0]
]

matrix = [[-2, 0, 3], [4, -5, 6]]
expected = [[-4, 0, 3], [8, -5, 12]]
result = transform(matrix)
assert result == expected


assert matrix == [[-2, 0, 3], [4, -5, 6]]

result[0][0] = 100

assert matrix[0][0] == -2

print("Все проверки пройдены!")
