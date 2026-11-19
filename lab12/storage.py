import json
import os

from logic import validate_records


class StorageError(Exception):
    ""


def load_records(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        raise
    except UnicodeDecodeError:
        raise StorageError("файл не в кодировке UTF-8") from None
    except json.JSONDecodeError as error:
        raise StorageError(f"повреждённый JSON: {error}") from None
    except OSError as error:
        raise StorageError(f"не удалось прочитать файл: {error}") from None
    try:
        validate_records(records)
    except ValueError as error:
        raise StorageError(f"неверная структура данных: {error}") from None
    return records


def save_records(path, records):
    try:
        validate_records(records)
    except ValueError as error:
        raise StorageError(f"нельзя сохранить: {error}") from None
    tmp_path = path + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
            file.write("\n")
        os.replace(tmp_path, path)
    except OSError as error:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise StorageError(f"не удалось сохранить: {error}") from None