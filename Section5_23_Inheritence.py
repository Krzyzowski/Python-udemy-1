
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f)

    def walk(self):
        print(f"{self.name} is walking.")

    def run(self):
        print(f"{self.name} is running.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} bark: Woof!")

    def run(self):
        print(f"{self.name} is running happily.")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows.")

    def walk(self):
        print(f"{self.name} is walking gracefully.")

# creating instances
buddy = Dog("Buddy")
whiskers = Cat("Whiskers")

# Dog behaviors

buddy.eat()
buddy.make_sound()
buddy.walk()
buddy.run()


# Cat behavior

whiskers.eat()
whiskers.make_sound()
whiskers.walk()
whiskers.run()