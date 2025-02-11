class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method for each instance
print(animal.speak())
print(dog.speak())
print(cat.speak())