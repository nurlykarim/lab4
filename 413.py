import json
import re

def query_json(data, query):
    pattern = re.compile(r'\.?([a-zA-Z_]\w*)|\[(\d+)\]')
    current = data
    for match in pattern.finditer(query):
        key, index = match.groups()
        try:
            if key:
                current = current[key]
            elif index:
                current = current[int(index)]
        except (KeyError, IndexError, TypeError):
            return "NOT_FOUND"
    return json.dumps(current, separators=(',', ':'))

# Чтение входа
data = json.loads(input())
q = int(input())
for _ in range(q):
    query = input()
    print(query_json(data, query))