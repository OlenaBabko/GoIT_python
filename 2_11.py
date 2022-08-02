class Developer:
    def __init__(self):
        self.fields = []

    def add(self, field_item):
        self.fields.append(field_item)  

    def delete(self, idx):
        self.fields.pop(idx)
        