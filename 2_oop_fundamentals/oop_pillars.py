import clases_and_objects as animals

# 1. Pillars of OOP

"""
    OOP stands for Object-Oriented Programming, a programming paradigm that uses "objects" to
    represent data and methods. The four main pillars of OOP are Encapsulation, Abstraction,
    Inheritance, and Polymorphism.
"""

# 1.1 Abstraction
"""
    Abstraction is the concept of hiding the complex implementation details and showing only the
    essential features of the object. It helps in reducing complexity and increases efficiency.
"""

class FlySimulator:
    """
        Only includes essential features for flying simulation.
    """
    def __init__(self, model, max_speed, fuel_capacity):
        self.model = model
        self.current_speed = 0
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.altitude = 0

    def take_off(self):
        print(f"✈️ {self.model} is taking off.")

    def fly(self):
        print(f"✈️ {self.model} is flying at {self.current_speed} km/h at an altitude of {self.altitude} meters.")

    def land(self):
        print(f"✈️ {self.model} is landing.")

class FlyReservation:
    """
        Only includes essential features for flight reservation.
    """
    def __init__(self, model, seat_capacity):
        self.model = model
        self.seat_capacity = seat_capacity
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.seat_capacity:
            self.booked_seats += 1
            print(f"✈️ Seat booked on {self.model}. Total booked seats: {self.booked_seats}")
        else:
            print(f"✈️ No seats available on {self.model}.")

print("Same plane model used for different purposes:")
flight_simulator = FlySimulator("Boeing 747", 900, 180000)
flight_reservation = FlyReservation("Boeing 747", 400)

flight_simulator.take_off()
flight_reservation.book_seat()

# 1.2 Encapsulation
"""
    Encapsulation is the concept of wrapping data and methods into a single unit, i.e., a class.
    It restricts direct access to some of the object's components and can prevent the accidental
    modification of data. This is typically done using access modifiers like private, protected,
    and public.
"""

class Car:
    """
        Hide internal details of the engine
    """
    def __init__(self, brand, model):
        # Public interface
        self.brand = brand
        self.model = model
        self.started = False

        # Private details
        self._engine_temperature = 20  # Protected attribute
        self.__oil_pressure = 30  # Private attribute

    def start(self):
        # Simple button to start the car
        print(f"🚗 {self.brand} {self.model} is starting.")
        self._start_engine()  # Internal method to start the engine
        self.started = True
        print("  🔥 Engine started.")

    def accelerate(self):
        """
            Simple pedal to accelerate the car.
        """
        if self.started:
            print(f" 🚗 {self.brand} {self.model} is accelerating.")
            self._rising_temperature() # Internal method to manage engine temperature
        else:
            print(f" 🚗 {self.brand} {self.model} is not started yet. Please start the car first.")
        

    # Private methods - Intern details hidden from the user
    def _start_engine(self):
        # The user doesn't need to know how the engine starts
        print("  🔧 Connecting circuits...")
        print("  🔧 Activating spark plugs...")
        print("  🔧 Initiating combustion...")
        self._engine_temperature = 90

    def _rising_temperature(self):
        # Internal method to manage engine temperature
        self._engine_temperature += 10
        if self._engine_temperature > 120:
            print("  ⚠️ Warning: Engine overheating! Automatically reducing speed.")

# E.g. of using the class
my_car = Car("Toyota", "Corolla")
my_car.start()
my_car.accelerate()

# 1.3 Inheritance
"""
    Inheritance is a mechanism where a new class inherits properties and behavior (methods) from
    an existing class. The existing class is called the "base" or "parent" class, and the new
    class is called the "derived" or "child" class. Inheritance promotes code reusability and
    establishes a natural hierarchy between classes.
"""

class Mammal(animals.Animal):
    """
        Intermediate level in the hierarchy
    """
    def __init__(self, name, sex, age, weight, color, texture):
        super().__init__(name, sex, age, weight, color, texture)
        self.texture = texture
        self.body_temperature = 37  # Mammals are warm-blooded

    def breastfeed(self):
        if self.sex == "female":
            print(f"🦁 {self.name} is breastfeeding her young.")

class PersianCat(animals.Cat, Mammal):
    def __init__(self, name, sex, age, weight, favorite_food):
        animals.Cat.__init__(self, name, sex, age, weight, "white", "long", favorite_food)
        self.texture = "long"
        self.purebread = True

# E.g.
# Complete hierarchy: Animal -> Mammal -> Cat -> PersianCat
persian_cat = PersianCat("Snowball", "female", 2, 4.5, "fish")
persian_cat.breathe() # Inherited from Animal
persian_cat.meow() # Inherited from Cat
persian_cat.breastfeed() # Inherited from Mammal

# 1.4 Polymorphism
"""
    Polymorphism allows methods to do different things based on the object it is acting upon,
    even if they share the same name. It allows for methods to be used interchangeably, making
    code more flexible and easier to maintain.
"""

def make_animal_concert(animal_list):
    """
        Function that takes a list of animals and makes them perform their unique sounds.
    """
    for animal in animal_list:
        print(f"🎤 Now in the stage: {animal.name}")
        animal.make_sound()

animal_bag = [
    animals.Cat("Whiskers", "female", 3, 4.0, "black", "short", "tuna"),
    animals.Dog("Buddy", "male", 5, 15.0, "golden", "short", "Labrador"),
    animals.Bird("Coco", "female", 2, 0.2, "green", "short", True),
    animals.Cat("Mittens", "male", 1, 2.5, "white", "long", "milk"),
    animals.Dog("Rex", "male", 7, 20.0, "black", "short", "German Shepherd")
]

make_animal_concert(animal_bag)