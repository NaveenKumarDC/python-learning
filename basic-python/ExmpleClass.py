class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog("Buddy")
print(f"{my_dog.name} says {my_dog.speak()}")
