import json

jsn ='''{
"0": {"fields": [
    {"value": "Vlad", "field_name": "Name"}, 
    {"value": 1300, "field_name": "Rate"}]}, 
"1": {"fields": [
    {"value": "Max", "field_name": "Name"}, 
    {"value": 1200, "field_name": "Rate"}]}, 
"2": {"fields": [
    {"value": "Ivan", "field_name": "Name"}, 
    {"value": 2800, "field_name": "Rate"}]}
}''' 

elem = json.loads(jsn)

name_3 = elem['2']['fields'][0]['value']
rate_1_2_3 = int(elem['0']['fields'][1]['value']) + int(elem['1']['fields'][1]['value']) + int(elem['2']['fields'][1]['value'])

print(name_3)
print(rate_1_2_3)