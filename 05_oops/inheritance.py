
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...")

class Dog(Animal):
    def speak(self):
        super().speak() # to call a method from a parent class
        print("woof!")

a = Animal("Dog")
a.speak()

d = Dog("Bruno")
d.speak()
