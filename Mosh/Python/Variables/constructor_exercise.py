class Person:
    def __init__(self, name):
        self.name = name 

    def talk(self):
        print(f"Hi, i'm {self.name}")


john = Person('SMITH John')
print(john.name)
john.talk()