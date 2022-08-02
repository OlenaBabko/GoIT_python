class Developer:
    def __init__(self): 
        self.fields = [] 


developer = Developer()

developer.fields.append('name')
developer.fields.append('city')
developer.fields.append('developer_skill')
developer.fields.append('rate')
developer.fields.append('phone')

developer.fields[2] = 'skill'

developer.fields.pop(4)
developer.fields.pop(3)

out = f"{developer.fields[0]} {developer.fields[1]} {developer.fields[2]}"