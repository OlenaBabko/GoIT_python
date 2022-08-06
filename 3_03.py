class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0


    def add(self, developer):
        self.developers[self.last_developer_id] = developer 
        self.last_developer_id += 1

    def delete(self,developer_id:int):
        key = int(developer_id)
        self.developers.pop(key)