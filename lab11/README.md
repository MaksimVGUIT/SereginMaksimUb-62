
## Файлы

| Файл | Назначение |
| --- | --- |
| `todos.json` | учебный набор из 5 задач |
| `analysis.py` | `validate_todos`, `completion_counts`, `top_users`, `leaders_tasks`, `select_tasks` |
| `main.py` | чтение, проверка, анализ, сводка, сохранение `leaders.json` и `selected.json` |
| `test_analysis.py` | 12 тестов без сети и без файлов проекта |
| `fetch_profile.py` | HTTP-упражнение (профиль GitHub по логину) |
| `profile_sample.json`, `read_sample.py` | офлайн-режим упражнения |

## Запуск

```
python main.py                  # спросит user_id
python fetch_profile.py         # нужен интернет
python read_sample.py           # без интернета
```

## Результаты

- Выполнено задач: `{5: 2, 10: 2}`, лидеры `[5, 10]`.
- `leaders.json`: задачи с id `[1, 3, 4, 5]`.
- `selected.json` при `user_id=5`: id `[2]` (совпадает с таблицей варианта 3); при `user_id=10` и неизвестном пользователе — `[]`.
- Повреждённый `todos.json`: сообщение об ошибке, `leaders.json` и `selected.json` не перезаписываются.

## HTTP-упражнение

- **Адрес** `https://api.github.com/users/<логин>` определяет ресурс — профиль пользователя; логин кодируется через `quote`.
- **GET** — метод чтения: запрос ничего не изменяет на сервере.
- **Таймаут 10 с** не даёт программе зависнуть, если сервер не отвечает.
- **Обработчики:** `HTTPError` — сервер ответил статусом ошибки (404, 403, 429); `URLError`/`TimeoutError` — нет сети или ответа; `ValueError`/`UnicodeError` — ответ не JSON или не профиль; `OSError` — ошибка записи `profile.json`.
- Запрос для `octocat`: _не выполнялся / результат: ..._ (заполните сами).
- Офлайн-режим: использованы учебные локальные данные `profile_sample.json`, логин `demo`.
