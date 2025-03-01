class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hello, My name is {self.name}.")

James = Person("James")
James.talk()