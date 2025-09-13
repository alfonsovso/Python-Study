class Pet():

    # Class variable (Means it's shared by all pets)
    available_species = ["dog", "cat", "bird", "fish"]

    """
        __init__ is a special method that runs when we create a new pet
        It's kind of like the 'birth certificate' of our pet
    """
    def __init__(self, species, name, age = 1):

        # Public attributes
        self.species = species
        self.name = name
        self.age = age
        self.happiness = 50
        self.energy = 100

        # Private attributes
        self._health = 100

        # Very private attributes
        self.__secret_id = f"{name}_{species}_2025"

        print(f"{self.name} has been born! It is a {self.species} of {self.age} year(s)")

    def __str__(self):
        """
            Special method that shows the state of our pet when we print it
            *** What we decide to display when 'print' is used ***
            We could see it as its stats
        """
        return f"🐾 {self.name} ({self.species}) - Happiness: {self.happiness}/100, Energy: {self.energy}/100"
    
    def __len__(self):
        """
            Special method that shows our pet's age
            *** What we decide to display when len() is used ***
        """
        return self.age
    
    def play(self):
        # Public method to play with the pet

        if self.energy >= 20:
            self.happiness += 15
            self.energy -= 20
            print(f"{self.name} is playing!")
            self._check_limits()
        else:
            print(f"{self.name} is too tired to play 😴")

    def feed(self):
        # Public method to feed the pet

        self.energy += 30
        self.happiness += 10
        print(f"{self.name} is eating! 🍖")
        self._check_limits()

    def sleep(self):
        # Public method for the pet to sleep

        self.energy = 100
        self.happiness += 5
        print(f"{self.name} is sleeping... ZZZ 😴")
        self._check_limits()

    def _check_limits(self):
        """
            This is a private method (we see that it starts with a single underscore '_')
            It is only used inside the class to check that values don't exceed their limits
        """

        if self.happiness > 100:
            self.happiness = 100
        if self.energy > 100:
            self.energy = 100
        if self.happiness < 0:
            self.happiness = 0
        if self.energy < 0:
            self.energy = 0

    def __get_secret_id(self):
        """
            This is a very private or secret method (it starts with two underscores '__')
            It can only be used inside this class 'Pet'
        """

        return self.__secret_id
    
    def show_full_info(self):
        # Method that shows the complete information of our pet, including private data

        print(f"Information about {self.name}")
        print(f"    Species: {self.species}")
        print(f"    Age: {self.age}")
        print(f"    Happiness: {self.happiness}")
        print(f"    Energy: {self.energy}")
        print(f"    Health: {self._health}")
        print(f"    Secret ID: {self.__get_secret_id()}")

# ========== USAGE EXAMPLES ==========

# To create a pet
my_dog = Pet("dog", "Everest", 3)

# See our pet
print(my_dog)

# Play with our pet
my_dog.play()
my_dog.play() # We can play with our pet as long as it has enough energy

# Feed our pet
my_dog.feed()

# ========== USE OF SPECIAL FUNCTIONS ==========

"""
    See our pet 
    (We already did it before; it's just to clarify that it is a special function 
    it has double underscores at the beginning and at the end)
"""
print (my_dog)

# We also use a special function to see its age
print(f"My dog is {len(my_dog)} years old")

# ========= SEE THE FULL INFORMATION =========
my_dog.show_full_info()
