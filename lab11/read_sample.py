import json
from pathlib import Path

path = Path(__file__).resolve().parent / "profile_sample.json"
with open(path, "r", encoding="utf-8") as file:
    profile = json.load(file)
print("Использованы учебные локальные данные.")
print("Логин:", profile["login"])