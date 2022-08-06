class DataField:
    field_description = "General"
    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}: {self.value}"

class FirstNameField(DataField):
    field_description = "Name"

class RateField(DataField):
    field_description = "Rate"


REGISTERED_FIELDS = {
    FirstNameField.field_description: FirstNameField,
    RateField.field_description: RateField
    }

def field_decoder(json_in):
    name = json_in["field_name"] 
    value = json_in["value"] 

    base_class = REGISTERED_FIELDS[name] 
    field = base_class(value)
    return field 
