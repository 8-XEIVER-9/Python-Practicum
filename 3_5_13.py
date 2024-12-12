from sys import stdin
import json
js = input()
with open(js, "r", encoding="UTF-8") as old:
    data = json.load(old)
new_data = stdin.readlines()
for new in new_data:
    key, value = new.split(" == ")
    data[key] = value.rstrip()
with open(js, "w", encoding="UTF-8") as ans:
    json.dump(data, ans, ensure_ascii=False, indent=4)