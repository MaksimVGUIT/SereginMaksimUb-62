import os
import sys

import logic
import storage

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

MENU = """
=== План покупок ===
1. Показать записи
2. Добавить запись
3. Найти записи
4. Изменить статус
5. Удалить запись
6. Показать статистику
7. Сохранить данные
8. Выйти"""


def status_text(record):
    return "куплено" if record["completed"] else "не куплено"


def show_records(records):
    if not records:
        print("Нет записей")
        return
    print_list(sorted(records, key=lambda r: r["id"]))


def print_list(records):
    for r in records:
        print(f"[{r['id']}] {r['title']} | {r['category']} | "
              f"{r['amount']} руб. | {status_text(r)}")


def ask_nonempty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Значение не должно быть пустым.")


def ask_amount(prompt):
    while True:
        try:
            return logic.parse_amount(input(prompt))
        except ValueError as error:
            print(f"Ошибка: {error}.")


def ask_id(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("ID должен быть целым числом.")
        return None


def add(records):
    title = ask_nonempty("Название: ")
    category = ask_nonempty("Категория: ")
    amount = ask_amount("Стоимость (целых рублей): ")
    record = logic.add_record(records, title, category, amount)
    print(f"Добавлено: запись с ID {record['id']}.")


def search(records):
    query = input("Что искать в названии: ")
    try:
        found = logic.find_records(records, query)
    except ValueError as error:
        print(f"Ошибка: {error}.")
        return
    if found:
        print_list(found)
    else:
        print("Ничего не найдено.")


def change_status(records):
    record_id = ask_id("ID записи: ")
    if record_id is None:
        return
    while True:
        choice = input("Новый статус: 1 — куплено, 2 — не куплено: ").strip()
        if choice in ("1", "2"):
            break
        print("Введите 1 или 2.")
    if logic.set_completed(records, record_id, choice == "1"):
        print("Статус изменён.")
    else:
        print(f"Записи с ID {record_id} нет.")


def delete(records):
    record_id = ask_id("ID записи для удаления: ")
    if record_id is None:
        return
    if not any(r["id"] == record_id for r in records):
        print(f"Записи с ID {record_id} нет.")
        return
    answer = input("Удалить? Введите «да» для подтверждения: ").strip().lower()
    if answer == "да":
        logic.delete_record(records, record_id)
        print("Запись удалена.")
    else:
        print("Удаление отменено.")


def show_statistics(records):
    stats = logic.statistics(records)
    print(f"Всего записей: {stats['total']}")
    print(f"Куплено: {stats['done']}")
    print(f"Не куплено: {stats['not_done']}")
    print(f"Общая сумма: {stats['total_amount']} руб.")
    if stats["by_category"]:
        print("По категориям:")
        for category, total in stats["by_category"].items():
            print(f"  {category}: {total} руб.")


def save(records):
    try:
        storage.save_records(DATA_PATH, records)
    except storage.StorageError as error:
        print(f"Ошибка: {error}.")
        return False
    print("Данные сохранены.")
    return True


def exit_program(records):
    while True:
        answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            if save(records):
                return True
            print("Остаёмся в меню.")
            return False
        if answer == "нет":
            return True
        print("Ответьте «да» или «нет».")


def load_at_start():
    try:
        return storage.load_records(DATA_PATH)
    except FileNotFoundError:
        print("Файл data.json не найден, начинаем с пустого списка.")
        return []
    except storage.StorageError as error:
        print(f"Не удалось загрузить data.json: {error}.")
        print("Файл не изменён. Исправьте его и запустите программу снова.")
        sys.exit(1)


def main():
    records = load_at_start()
    actions = {
        "1": show_records, "2": add, "3": search, "4": change_status,
        "5": delete, "6": show_statistics, "7": save,
    }
    while True:
        print(MENU)
        command = input("Команда: ").strip()
        if command == "8":
            if exit_program(records):
                break
        elif command in actions:
            actions[command](records)
        else:
            print("Неизвестная команда, попробуйте ещё раз.")


if __name__ == "__main__":
    main()
