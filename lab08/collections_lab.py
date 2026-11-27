def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        cleaned = word.strip(".,!?;:")
        if cleaned == "":
            continue
        counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")

def common_topics(first, second):
    first_set = set(first)
    second_set = set(second)

    return sorted(first_set & second_set)


def all_topics(first, second):
    first_set = set(first)
    second_set = set(second)

    return sorted(first_set | second_set)


def create_record():
    record = {
        "title": "Python",
        "hours": 4
    }

    record["hours"] = 6
    record["completed"] = False

    pair = (record["title"], record["hours"])
    title, hours = pair

    print("Учебная запись:", record)
    print("Кортеж:", pair)
    print("Название:", title)
    print("Количество часов:", hours)


def totals_by_category(records):
    totals = {}

    for record in records:
        category = record["category"]
        amount = record["amount"]

        totals[category] = totals.get(category, 0) + amount

    return totals


def titles_in_category(records, category):
    titles = []

    for record in records:
        if record["category"] == category:
            titles.append(record["title"])

    return titles


def sorted_totals(records):
    totals = totals_by_category(records)

    return sorted(
        totals.items(),
        key=lambda item: (-item[1], item[0])
    )

def main():
    # Подсчёт частоты слов
    text = input("Введите текст для подсчёта слов: ")
    counts = word_counts(text)

    print("Частота слов:")
    print_word_counts(counts)

    # Работа с учебными интересами
    first = ["python", "sql", "python"]
    second = ["sql", "git"]

    print("Общие учебные темы:", common_topics(first, second))
    print("Все учебные темы:", all_topics(first, second))

    # Создание словаря и кортежа
    create_record()

    # Записи о покупках, вариант № 3
    records = [
        {"title": "Хлеб", "category": "основное", "amount": 56},
        {"title": "Молоко", "category": "основное", "amount": 89},
        {"title": "арбуз", "category": "дополнительное", "amount": 40},
        {"title": "кофе", "category": "бытовое", "amount": 105},
        {"title": "Чай", "category": "дополнительное", "amount": 160}
    ]

    print("Суммы по категориям:")

    totals = totals_by_category(records)

    for category in sorted(totals):
        print(f"{category}: {totals[category]} руб.")

    category = input("Введите категорию для поиска покупок: ")

    print("Покупки в выбранной категории:")
    print(titles_in_category(records, category))

    # Дополнительное задание
    print("Категории по убыванию суммы:")
    print(sorted_totals(records))


if __name__ == "__main__":
    main()