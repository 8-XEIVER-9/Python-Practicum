import json
json_name = input()
json_update = input()
with open(json_name) as file:
    olds = json.load(file)
with open(json_update) as file:
    news = json.load(file)
name_key = 'name'
new_dict = {}
for new in news:
    for old in olds:
        if new[name_key] == old[name_key]:
            for key in new.keys():
                if new[key] > old.get(key, ''):
                    old[key] = new[key]
for old in olds:
    name = old.pop(name_key)
    new_dict[name] = old
with open(json_name, 'w') as file:
    json.dump(new_dict, file, indent=4, ensure_ascii=False)