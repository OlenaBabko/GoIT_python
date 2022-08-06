import json
class DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}:{self.value}"

class FirstNameField(DataField):   
    field_description = "Name"  

jsn ='{"value": "Ivan", "field_name": "Name"}'

elem = json.loads(jsn)
value = elem['value']

obj = FirstNameField(value)
print(obj)