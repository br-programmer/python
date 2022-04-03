class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
user = User('Brayan', 24, 'Male') 

print(user.name)
print(user.age)
print(user.gender)
