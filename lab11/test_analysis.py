import copy
import json
import os
import unittest
from tempfile import TemporaryDirectory

import analysis

TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]


def ids(items):
    return [t["id"] for t in items]


class TestAnalysis(unittest.TestCase):
    def test_sample_counts_and_leaders(self):
        counts = analysis.completion_counts(TODOS)
        self.assertEqual(counts, {5: 2, 10: 2})
        leaders = analysis.top_users(counts)
        self.assertEqual(leaders, [5, 10])
        self.assertEqual(ids(analysis.leaders_tasks(TODOS, leaders)), [1, 3, 4, 5])

    def test_empty(self):
        self.assertEqual(analysis.completion_counts([]), {})
        self.assertEqual(analysis.top_users({}), [])
        self.assertEqual(analysis.leaders_tasks([], []), [])

    def test_only_unfinished(self):
        todos = [dict(t, completed=False) for t in TODOS]
        counts = analysis.completion_counts(todos)
        self.assertEqual(counts, {5: 0, 10: 0})   # пользователи с нулём остаются
        leaders = analysis.top_users(counts)
        self.assertEqual(leaders, [])
        self.assertEqual(analysis.leaders_tasks(todos, leaders), [])

    def test_single_leader(self):
        todos = [TODOS[0], TODOS[4], TODOS[2]]
        counts = analysis.completion_counts(todos)
        self.assertEqual(counts, {5: 2, 10: 1})
        self.assertEqual(analysis.top_users(counts), [5])

    def test_several_leaders_sorted(self):
        self.assertEqual(analysis.top_users({10: 3, 5: 3, 7: 1}), [5, 10])

    # --- вариант 3 ---
    def test_select_sample(self):
        self.assertEqual(ids(analysis.select_tasks(TODOS, 5)), [2])
        self.assertEqual(ids(analysis.select_tasks(TODOS, 5, None)), [2])

    def test_select_unknown_user(self):
        self.assertEqual(analysis.select_tasks(TODOS, 99), [])

    def test_select_no_match(self):
        self.assertEqual(analysis.select_tasks(TODOS, 10), [])  # все завершены

    def test_select_keeps_order_and_data(self):
        todos = [
            {"id": 7, "userId": 1, "title": "a", "completed": False},
            {"id": 3, "userId": 1, "title": "b", "completed": False},
            {"id": 4, "userId": 2, "title": "c", "completed": False},
            {"id": 5, "userId": 1, "title": "d", "completed": True},
        ]
        before = copy.deepcopy(todos)
        self.assertEqual(ids(analysis.select_tasks(todos, 1)), [7, 3])
        self.assertEqual(todos, before)

    # --- проверка структуры ---
    def test_validate_ok(self):
        analysis.validate_todos(TODOS)
        analysis.validate_todos([])
        extra = copy.deepcopy(TODOS)
        extra[0]["note"] = "x"
        analysis.validate_todos(extra)

    def test_validate_errors(self):
        base = TODOS[0]
        dup = copy.deepcopy(TODOS)
        dup[1]["id"] = 1
        no_user = {k: v for k, v in base.items() if k != "userId"}
        cases = {
            "объект вместо списка": {"id": 1},
            "повторный id": dup,
            "нет userId": [no_user],
            "completed строкой": [dict(base, completed="false")],
            "id=true": [dict(base, id=True)],
            "userId=true": [dict(base, userId=True)],
            "id нулевой": [dict(base, id=0)],
            "пустой title": [dict(base, title="  ")],
            "запись не словарь": ["строка"],
        }
        for name, data in cases.items():
            with self.subTest(name):
                with self.assertRaises(ValueError):
                    analysis.validate_todos(data)

    def test_json_roundtrip(self):
        selected = analysis.select_tasks(TODOS, 5)
        with TemporaryDirectory() as folder:
            path = os.path.join(folder, "selected.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(selected, f, ensure_ascii=False, indent=2)
            with open(path, encoding="utf-8") as f:
                self.assertEqual(json.load(f), selected)


if __name__ == "__main__":
    unittest.main()
