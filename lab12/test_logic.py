import unittest

import logic


def sample():
    return [
        {"id": 1, "title": "Python", "category": "книги", "amount": 4, "completed": False},
        {"id": 2, "title": "Хлеб", "category": "еда", "amount": 2, "completed": True},
    ]


class TestLogic(unittest.TestCase):
    def test_empty_statistics(self):
        self.assertEqual(logic.statistics([]), {
            "total": 0, "done": 0, "not_done": 0,
            "total_amount": 0, "by_category": {}})

    def test_statistics_two_categories(self):
        stats = logic.statistics(sample())
        self.assertEqual(stats["total"], 2)
        self.assertEqual(stats["done"], 1)
        self.assertEqual(stats["not_done"], 1)
        self.assertEqual(stats["total_amount"], 6)
        self.assertEqual(list(stats["by_category"].items()), [("еда", 2), ("книги", 4)])

    def test_statistics_strips_category(self):
        records = sample()
        records[1]["category"] = " книги "
        self.assertEqual(logic.statistics(records)["by_category"], {"книги": 6})

    def test_add_strips_and_sets_status(self):
        records = []
        rec = logic.add_record(records, " Python ", " книги ", 5)
        self.assertEqual(rec["title"], "Python")
        self.assertEqual(rec["category"], "книги")
        self.assertIs(rec["completed"], False)
        self.assertEqual(rec["id"], 1)

    def test_add_duplicate_titles(self):
        records = []
        logic.add_record(records, "Хлеб", "еда", 1)
        logic.add_record(records, "Хлеб", "еда", 1)
        self.assertEqual([r["id"] for r in records], [1, 2])

    def test_add_invalid_does_not_change(self):
        records = sample()
        for args in [("  ", "еда", 1), ("a", "  ", 1), ("a", "b", -1),
                     ("a", "b", True), ("a", "b", "5"), ("a", "b", 1.5)]:
            with self.assertRaises(ValueError):
                logic.add_record(records, *args)
        self.assertEqual(records, sample())

    def test_ids_after_delete(self):
        records = sample()
        self.assertTrue(logic.delete_record(records, 1))
        self.assertEqual(records[0]["id"], 2)
        self.assertEqual(logic.add_record(records, "Новое", "еда", 1)["id"], 3)

    def test_find_case_insensitive(self):
        self.assertEqual(len(logic.find_records(sample(), "PY")), 1)
        self.assertEqual(len(logic.find_records(sample(), "ХЛЕБ")), 1)
        self.assertEqual(logic.find_records(sample(), "zzz"), [])

    def test_find_empty_query(self):
        for q in ("", "   "):
            with self.assertRaises(ValueError):
                logic.find_records(sample(), q)

    def test_find_does_not_change(self):
        records = sample()
        logic.find_records(records, "py")
        self.assertEqual(records, sample())

    def test_set_completed(self):
        records = sample()
        self.assertTrue(logic.set_completed(records, 1, True))
        self.assertIs(records[0]["completed"], True)
        self.assertTrue(logic.set_completed(records, 1, True))  # явная установка
        self.assertIs(records[0]["completed"], True)

    def test_set_completed_unknown_id(self):
        records = sample()
        self.assertFalse(logic.set_completed(records, 99, True))
        self.assertEqual(records, sample())

    def test_delete_unknown_id(self):
        records = sample()
        self.assertFalse(logic.delete_record(records, 99))
        self.assertEqual(records, sample())

    def test_strict_types(self):
        bad = [
            {"id": True, "title": "a", "category": "b", "amount": 1, "completed": False},
            {"id": 0, "title": "a", "category": "b", "amount": 1, "completed": False},
            {"id": 1, "title": " ", "category": "b", "amount": 1, "completed": False},
            {"id": 1, "title": "a", "category": 5, "amount": 1, "completed": False},
            {"id": 1, "title": "a", "category": "b", "amount": True, "completed": False},
            {"id": 1, "title": "a", "category": "b", "amount": -1, "completed": False},
            {"id": 1, "title": "a", "category": "b", "amount": 1.0, "completed": False},
            {"id": 1, "title": "a", "category": "b", "amount": 1, "completed": 0},
            {"id": 1, "title": "a", "category": "b", "amount": 1},
            "строка",
        ]
        for record in bad:
            with self.subTest(record=record):
                with self.assertRaises(ValueError):
                    logic.validate_records([record])

    def test_validate_set(self):
        logic.validate_records([])
        logic.validate_records(sample())
        with self.assertRaises(ValueError):
            logic.validate_records({})
        dup = sample()
        dup[1]["id"] = 1
        with self.assertRaises(ValueError):
            logic.validate_records(dup)

    def test_extra_keys_allowed(self):
        records = sample()
        records[0]["note"] = "x"
        logic.validate_records(records)

    def test_parse_amount(self):
        self.assertEqual(logic.parse_amount(" 12 "), 12)
        self.assertEqual(logic.parse_amount("0"), 0)
        for text in ("abc", "-1", "", "1.5"):
            with self.assertRaises(ValueError):
                logic.parse_amount(text)


if __name__ == "__main__":
    unittest.main()
