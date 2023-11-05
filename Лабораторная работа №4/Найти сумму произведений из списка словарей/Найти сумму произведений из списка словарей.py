# TODO решите задачу
import json

FILENAME = 'input.json'

def task(FILENAME) -> float:
    count = 0
    with open(FILENAME, 'r') as f:
        data = json.load(f)
        for k in data:
            count += k['score'] * k['weight']
    return round(count, 3)


print(task(FILENAME))
