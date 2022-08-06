import json
lst = []

lst.append(5)
lst.append(6)
lst.append(7)
lst.append(8)
jsn = json.dumps(lst)
print(jsn)