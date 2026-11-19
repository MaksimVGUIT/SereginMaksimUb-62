def _is_int(value):
    return type(value) is int

def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("корень JSON должен быть списком")
    seen_ids = set()
    for number, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"запись №{number}: должна быть объектом")
        for key in ("id", "userId", "title", "completed"):
            if key not in item:
                raise ValueError(f"запись №{number}: нет ключа «{key}»")
        if not _is_int(item["id"]) or item["id"] <= 0:
            raise ValueError(f"запись №{number}: id должен быть положительным целым")
        if not _is_int(item["userId"]) or item["userId"] <= 0:
            raise ValueError(f"запись №{number}: userId должен быть положительным целым")
        if not isinstance(item["title"], str) or not item["title"].strip():
            raise ValueError(f"запись №{number}: title должен быть непустой строкой")
        if type(item["completed"]) is not bool:
            raise ValueError(f"запись №{number}: completed должен быть true/false")
        if item["id"] in seen_ids:
            raise ValueError(f"запись №{number}: повторяющийся id {item['id']}")
        seen_ids.add(item["id"])


def completion_counts(todos):
    counts = {}
    for todo in todos:
        user = todo["userId"]
        counts[user] = counts.get(user, 0) + (1 if todo["completed"] else 0)
    return counts


def top_users(counts):
    if not counts:
        return []
    best = max(counts.values())
    if best == 0:
        return []
    return sorted(user for user, value in counts.items() if value == best)


def leaders_tasks(todos, leaders):
    return [t for t in todos if t["completed"] and t["userId"] in leaders]


def select_tasks(todos, user_id, parameter=None):
    return [t for t in todos if t["userId"] == user_id and not t["completed"]]