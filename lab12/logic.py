REQUIRED_KEYS = ("id", "title", "category", "amount", "completed")


def _is_int(value):
    return type(value) is int


def _is_text(value):
    return isinstance(value, str) and value.strip() != ""


def validate_record(record):
    if not isinstance(record, dict):
        raise ValueError("запись должна быть словарём")
    for key in REQUIRED_KEYS:
        if key not in record:
            raise ValueError(f"нет обязательного ключа «{key}»")
    if not _is_int(record["id"]) or record["id"] <= 0:
        raise ValueError("id должен быть положительным целым числом")
    if not _is_text(record["title"]):
        raise ValueError("title должен быть непустой строкой")
    if not _is_text(record["category"]):
        raise ValueError("category должна быть непустой строкой")
    if not _is_int(record["amount"]) or record["amount"] < 0:
        raise ValueError("amount должен быть целым числом не меньше нуля")
    if type(record["completed"]) is not bool:
        raise ValueError("completed должен быть логическим значением")


def validate_records(records):
    if not isinstance(records, list):
        raise ValueError("корень данных должен быть списком")
    seen = set()
    for number, record in enumerate(records, start=1):
        try:
            validate_record(record)
        except ValueError as error:
            raise ValueError(f"запись №{number}: {error}") from None
        if record["id"] in seen:
            raise ValueError(f"запись №{number}: повторяющийся id {record['id']}")
        seen.add(record["id"])


def parse_amount(text):
    try:
        value = int(text.strip())
    except (ValueError, AttributeError):
        raise ValueError("введите целое число") from None
    if value < 0:
        raise ValueError("стоимость не может быть отрицательной")
    return value


def next_id(records):
    return max((r["id"] for r in records), default=0) + 1


def add_record(records, title, category, amount):
    if not isinstance(title, str) or not isinstance(category, str):
        raise ValueError("название и категория должны быть строками")
    record = {
        "id": next_id(records),
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    validate_record(record)
    records.append(record)
    return record


def find_records(records, query):
    if not isinstance(query, str) or query.strip() == "":
        raise ValueError("поисковый запрос не должен быть пустым")
    needle = query.strip().casefold()
    return [r for r in records if needle in r["title"].casefold()]


def set_completed(records, record_id, completed):
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    done = sum(1 for r in records if r["completed"])
    totals = {}
    for r in records:
        key = r["category"].strip()
        totals[key] = totals.get(key, 0) + r["amount"]
    return {
        "total": len(records),
        "done": done,
        "not_done": len(records) - done,
        "total_amount": sum(r["amount"] for r in records),
        "by_category": dict(sorted(totals.items())),
    }