# TODO решите задачу
import json

file_ = "input.json"

def task() -> float:
    with open(file_, 'r', encoding='utf-8') as file:
        data = json.load(file)
        total = sum(item['score'] * item['weight'] for item in data)
        return round(total, 3)


print(task())
