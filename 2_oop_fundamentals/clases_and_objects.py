# 1. Clases and Objects in Python

class Animal:

    """
        Clase base Animal
        Al igual que en el libro 'Sumergete en los patrones de diseño' de Alexander Shvets,
        una clase es como un plano que define la estructura de los objetos
    """

    def __init__(self, name, sex, age, weight, color, texture):

        # Attributes or also called FIELDS (state)
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.color = color
        self.texture = texture
        print(f"🐾 Born {name}, a {sex} of {age} year(s)")

    def breath(self):
        print(f"{self.name} is breathing...💨")

    def sleep(self):
        print(f"{self.name} is sleeping...💤")

    def eat(self):
        print(f"{self.name} is eating...🍽️")

    def move(self):
        print(f"{self.name} is moving...🏃‍♂️")

    def make_sound(self):
        print(f"{self.name} is making a sound...🔊")

# E.g.
# Create objects (instances) of the Animal class
# Oscar and Luna are objects (instances) of the Animal class
oscar = Animal("Oscar", "male", 3, 7, "brown", "stripes")
luna = Animal("Luna", "female", 2, 5, "gray", "smooth")

print(f"Oscar: {oscar.name}, {oscar.sex}, {oscar.age} years old, {oscar.weight} kg, {oscar.color}, {oscar.texture}")
print(f"Luna: {luna.name}, {luna.sex}, {luna.age} years old, {luna.weight} kg, {luna.color}, {luna.texture}")

# Call methods on the objects
oscar.breath()
oscar.eat()
luna.move()
luna.make_sound()

# 2. Hierarchy of Classes (Inheritance)

class Cat(Animal):

    """
        As the book says: "Subclasses inherit state and behavior from their parent 
        and merely define different attributes or behaviors."
    """

    def __init__(self, name, sex, age, weight, color, texture, favorite_food):
        # Call the constructor of the parent class (superclass)
        super().__init__(name, sex, age, weight, color, texture)

        # Additional attribute for Cat
        self.favorite_food = favorite_food
        self.lives = 9  # Cats are said to have 9 lives

    def meow(self):
        print(f"{self.name} says Meow! 🐱")

    def make_sound(self):
        self.meow()  # Override the make_sound method of the superclass

    def purr(self):
        print(f"{self.name} is purring... Purrr purrr 😻")

class Dog(Animal):

    """
        Dog class inheriting from Animal
    """

    def __init__(self, name, sex, age, weight, color, texture, breed):
        super().__init__(name, sex, age, weight, color, texture)
        self.breed = breed
        self.loyalty = 100  # Dogs are known for their loyalty

    def bark(self):
        print(f"{self.name} says Woof! 🐶")

    def make_sound(self):
        self.bark()  # Override the make_sound method of the superclass

    def wag_tail(self):
        print(f"{self.name} is wagging its tail... 🐕‍🦺")

class Bird(Animal):

    """
        Bird class inheriting from Animal
    """

    def __init__(self, name, sex, age, weight, color, texture, can_fly=True):
        super().__init__(name, sex, age, weight, color, texture)
        self.can_fly = can_fly

    def chirp(self):
        print(f"{self.name} says Chirp! 🐦")

    def make_sound(self):
        self.chirp()  # Override the make_sound method of the superclass

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying... 🕊️")
        else:
            print(f"{self.name} cannot fly. 🐥")

# E.g.
# Create instances of Cat, Dog, and Bird

garfield = Cat("Garfield", "male", 5, 8, "orange", "tabby", "lasagna")
fido = Dog("Fido", "male", 4, 10, "brown", "smooth", "Golden Retriever")
tweety = Bird("Tweety", "female", 2, 1, "yellow", "feathery", True)

# Clases inerited from Animal can use its methods
garfield.eat()
fido.breath()
tweety.sleep()

# Each subclass can use its own methods
garfield.meow()
fido.bark()
tweety.chirp()