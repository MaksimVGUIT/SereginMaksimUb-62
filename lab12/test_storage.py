import json
import os
import unittest
from tempfile import TemporaryDirectory

import storage


def sample():
    return [
        {"id": 1, "title": "Молоко", "category": "еда", "amount": 90, "completed": True},
        {"id": 3, "title": "Блокнот", "category": "канцелярия", "amount": 150, "completed": False},
    ]


class TestStorage(unittest.TestCase):
    def test_roundtrip(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            storage.save_records(path, sample())
            self.assertEqual(storage.load_records(path), sample())

    def test_utf8_not_escaped(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            storage.save_records(path, sample())
            with open(path, encoding="utf-8") as f:
                self.assertIn("Молоко", f.read())

    def test_empty_list(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            storage.save_records(path, [])
            self.assertEqual(storage.load_records(path), [])

    def test_missing_file(self):
        with TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                storage.load_records(os.path.join(folder, "none.json"))

    def test_broken_json_not_modified(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            with open(path, "w", encoding="utf-8") as f:
                f.write("[{broken")
            with self.assertRaises(storage.StorageError):
                storage.load_records(path)
            with open(path, encoding="utf-8") as f:
                self.assertEqual(f.read(), "[{broken")

    def test_wrong_encoding(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            with open(path, "wb") as f:
                f.write("[]".encode("utf-16"))
            with self.assertRaises(storage.StorageError):
                storage.load_records(path)

    def test_bad_structure_and_duplicate_id(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            dup = sample()
            dup[1]["id"] = 1
            for content in ({"a": 1}, dup):
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(content, f)
                with self.assertRaises(storage.StorageError):
                    storage.load_records(path)

    def test_save_error(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "нет_папки", "data.json")
            with self.assertRaises(storage.StorageError):
                storage.save_records(path, sample())

    def test_save_invalid_data_keeps_old_file(self):
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            storage.save_records(path, sample())
            with self.assertRaises(storage.StorageError):
                storage.save_records(path, [{"id": 1}])
            self.assertEqual(storage.load_records(path), sample())


if __name__ == "__main__":
    unittest.main()
