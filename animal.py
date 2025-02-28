class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name, "says", dog.speak())
print(cat.name, "says", cat.speak())
