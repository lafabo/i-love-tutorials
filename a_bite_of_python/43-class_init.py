class Person:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print('Hello, my name is ', self.name)

p = Person('Boris')
p.sayhi()
