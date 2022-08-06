import json

developer1 = {'name': 'Max', 'rate': 1500 }
developer2 = {'name': 'Vlad', 'rate': 2300 }
developer3 = {'name': 'Ivan', 'rate': 2700 }

developer_list = [developer1,developer2,developer3]

jsn = json.dumps(developer_list)