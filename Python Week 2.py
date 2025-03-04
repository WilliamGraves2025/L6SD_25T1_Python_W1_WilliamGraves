print("\033[H\033[J", end="")

class Car:
    year = 2013
    make = "Leaf"
    model = "Leaf"

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def start_car():
        print("Car started successfully")

    start_car()

    def destroy():
        del c4
        print("c4 was deleted")

class Car10:
    def __init__(self, year, make, model):
        self.year = 2013
        self.make = "Nissan"
        self.model = "Leaf"

    def start_car():
        print("Car started successfully")
    
    start_car()
    
    c1 = Car(2013, "Nissan", "Leaf")
    c2 = Car(2018, "Tesla", "Model 3")
    c3 = Car(2021, "Tesla", "Cyber Truck")
    c4 = Car(2024, "Tesla", "Model X")

    print(c1.year, c1.make, c1.model)
    print(c2.year, c2.make, c2.model)
    print(c3.year, c3.make, c3.model)
    print(c4.year, c4.make, c4.model) 

class Person:
    name = "William"
    age = 19

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

p1 = Person("William", 18)
print(p1.name, p1.age)
del p1

class Task:
    def __init__(self, description):
        self.description = description
        print("Running task", description)

    def complete(self):
        print("Task", self.description, "complete!")

    def cleanup(self):
        print("Cleaning up")
        del self

task = Task("Firefighter")
task.complete()
task.cleanup()

class Rectangle:
    def __init__(self, length=1, width=1, *args):
        self.length = length
        self.width = width

r1 = Rectangle(1,2,4,6,8,9)
print(r1.length)
print(r1.width)
r2 = Rectangle()
print(r2.length)
print(r2.width)

class Animal0:
    def __init__(self):
        pass

    def make_sound(sound):
        print(sound)

class Dog(Animal0):
    def __init__(self):
        pass
    
Animal0.make_sound("Woof")

class Person:
    def __init__(self, name="William", age="19"):
        self.name = name
        self.age = age

class Skills(Person):
    def __init__(self, programming_skill=7, communication_skill=4):
        self.programming_skill = programming_skill
        self.communication_skill = communication_skill

class Employee(Skills, Person):
    def __init__(self):
        pass

class Vehicle:
    def start_engine():
        print("Engine started!")

Vehicle.start_engine()

class Car(Vehicle):
    def drive():
        print("Driving!")

Car.drive()

class ElectricCar(Car):
    def charge_battery():
        print("Battery charging!")

ElectricCar.charge_battery()

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound():
        print("Generic animal sound")

Animal.make_sound()

class Mammal(Animal):
    def __init__(self, name, species, fur_colour):
        super().__init__(name, species)
        self.fur_color = fur_colour

    def give_birth(self):
        print(f"{self.name} is giving birth")

# Mammal.give_birth()

class FireDog(Mammal):
    def __init__(self, name, species, fur_colour):
        super().__init__(name, species, fur_colour)
        self.name = "Firedog Radar"
        self.species = "Dalmation"
        self.fur_color = "Black and white"

    def become_fire_dog(self):
        print(f"{self.name} is becoming a fire dog")

# FireDog.become_fire_dog()

class Bird(Animal):
    def __init__(self, name, species, feather_color):
        super().__init__(name, species)
        self.feather_color = feather_color

    def fly(self):
        print(f"{self.name} is flying")

# Bird.fly()

class Subject:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"Studying {self.name}")

# Subject.study()

class Firefighting(Subject):
    def __init__(self, name, fires):
        super().__init__(name)
        self.fires = fires

    def extinguish_fires(self):
        print(f"Extinguishing {self.fires} fires")

# Firefighting.extinguish_fires()

class Math(Subject):
    def __init__(self, name, difficulty_level):
        super().__init__(name)
        self.difficulty_level = difficulty_level

    def solve_problem(self):
        print(f"Solving a {self.difficulty_level} math problem")

# Math.solve_problem()

class Language(Subject):
    def __init__(self, name, language_type):
        super().__init__(name)
        self.language_type = language_type

    def practice_language(self):
        print(f"Practicing {self.language_type} language")

# Language.practice_language()

shopping_list = []
shopping_list.insert(1, "apple")
shopping_list.insert(2, "banana")
shopping_list.insert(3, "orange")
print(shopping_list)
shopping_list.insert(4, "grapes")
shopping_list.remove("banana")
print(shopping_list)

coordinates = (41, 40)
print(coordinates)
coordinates = (41, 41)
print(coordinates)

fruits = ("avocado", "banana", "apple")
print(fruits[1])
if "banana" in fruits:
    print("Banana is in this tuple!")
else:
    print("Banana is not in this tuple")

library = {
    "Charlie and the Chocolate Factory": "Roald Dahl",
    "Charlie ad the Great Glass Elevator": "Roald Dahl"
}
print(library)

words = ["Firefighting", "Firefighter", "William", "The", "Fireman"]

dictionary = {}

for word in words:
    dictionary[word] = len(word)

print(dictionary)

words1 = ["Firefighting", "Firefighter", "William", "The", "Fireman"]
words2 = ["Firefighter", "William"]

output = set(words1).intersection(words2)
print(output)

words22 = ["Firefighting", "Firefighter", "William", "The", "Fireman", "Firefighting", "Firefighter", "William", "The", "Fireman"]

words222 = set(words22)
words2222 = list(words222)

print(words2222)

words3 = ["Firefighting", "Firefighter", "William", "The", "Fireman"]

stack = []

reverse = []

for word in words3:
    stack.append(word)

while stack:
        reverse.append(stack.pop())

print(reverse)

# ------------------------------ The rest of this has been skipped due to time constraints