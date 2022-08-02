class Developer:
    def __init__(self,name,phone):
        self.name = name
        self.city = 'Kyiv'
        self.skill = 'Python'
        self.rate = 1300
        self.phone = phone

user = Developer('Vlad','+380631234570')

out1 = f"{user.name} {user.phone}"
out2 = f"{user.name} {user.city} {user.skill} {user.rate} {user.phone}"