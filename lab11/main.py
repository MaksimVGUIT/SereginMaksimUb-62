import json
import sys
from pathlib import Path

import analysis

BASE = Path(__file__).resolve().parent


def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def ask_user_id():
    while True:
        text = input("Введите user_id (положительное целое): ").strip()
        try:
            value = int(text)
        except ValueError:
            print("Нужно целое число.")
            continue
        if value > 0:
            return value
        print("Число должно быть положительным.")


def main():
    try:
        todos = read_json(BASE / "todos.json")
        analysis.validate_todos(todos)
    except FileNotFoundError:
        print("Файл todos.json не найден.")
        return 1
    except UnicodeDecodeError:
        print("Файл todos.json не в кодировке UTF-8.")
        return 1
    except json.JSONDecodeError as error:
        print(f"Некорректный JSON: {error}")
        return 1
    except ValueError as error:
        print(f"Неверная структура данных: {error}")
        return 1
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return 1

    counts = analysis.completion_counts(todos)
    leaders = analysis.top_users(counts)
    leaders_data = analysis.leaders_tasks(todos, leaders)
    user_id = ask_user_id()
    selected = analysis.select_tasks(todos, user_id)

    print("Выполнено задач по пользователям:")
    for user in sorted(counts):
        print(f"  пользователь {user}: {counts[user]}")
    print("Лидеры:", ", ".join(str(u) for u in leaders) if leaders else "нет")
    print(f"Незавершённых задач пользователя {user_id}: {len(selected)}")

    try:
        write_json(BASE / "leaders.json", leaders_data)
        write_json(BASE / "selected.json", selected)
    except OSError as error:
        print(f"Не удалось сохранить результаты: {error}")
        return 1
    print("Результаты сохранены: leaders.json, selected.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
