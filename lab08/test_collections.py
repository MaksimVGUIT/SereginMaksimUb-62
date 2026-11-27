from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    sorted_totals
)


assert word_counts("Python, python! SQL") == {
    "python": 2,
    "sql": 1
}

assert word_counts("!!!") == {}
assert word_counts("") == {}
assert word_counts("Python Python Python") == {
    "python": 3
}


first = ["python", "sql", "python"]
second = ["sql", "git"]

assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python", "sql"]

assert common_topics([], ["python", "sql"]) == []
assert all_topics([], ["python", "sql"]) == ["python", "sql"]

assert common_topics(["python"], []) == []
assert all_topics(["python"], []) == ["python"]


records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3}
]

original = [record.copy() for record in records]

assert totals_by_category(records) == {
    "основное": 7,
    "дополнительное": 2
}

assert records == original

assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "дополнительное") == ["B"]
assert titles_in_category(records, "нет") == []

assert records == original
assert totals_by_category([]) == {}
assert titles_in_category([], "основное") == []


assert sorted_totals(records) == [
    ("основное", 7),
    ("дополнительное", 2)
]



shopping = [
    {"title": "Хлеб", "category": "основное", "amount": 56},
    {"title": "Молоко", "category": "основное", "amount": 89},
    {"title": "арбуз", "category": "дополнительное", "amount": 40},
    {"title": "кофе", "category": "бытовое", "amount": 105},
    {"title": "Чай", "category": "дополнительное", "amount": 160}
]

shopping_original = [record.copy() for record in shopping]

assert totals_by_category(shopping) == {
    "основное": 145,
    "дополнительное": 200,
    "бытовое": 105
}

assert titles_in_category(shopping, "основное") == [
    "Хлеб", "Молоко"
]

assert titles_in_category(shopping, "дополнительное") == [
    "арбуз", "Чай"
]

assert titles_in_category(shopping, "бытовое") == ["кофе"]

assert sorted_totals(shopping) == [
    ("дополнительное", 200),
    ("основное", 145),
    ("бытовое", 105)
]

assert shopping == shopping_original

print("Все проверки пройдены")
