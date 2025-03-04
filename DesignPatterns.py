class PresidentOffice:
    instance = None
    president = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(PresidentOffice, cls).__new__(cls)
            cls.president = "John Doe"
        return cls.instance
    
    def meetpresident(self, visitorname):
        print("f*{visitorname} is visiting President {self.president}")

office1 = PresidentOffice()
office2 = PresidentOffice()

office1.meetpresident("Alice")
office2.meetpresident("Bob")

print(office1 is office2)


class Pizza:
    def prepare(self):
        pass

class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

class VegetarianPizza(Pizza):
    def prepare(self):
        print("Preparing Vegetarian Pizza")

class PizzaFactory:
    def createpizza(self, pizzatype):
        if pizzatype == "Margherita":
            return MargheritaPizza()
        elif pizzatype == "Pepperoni":
            return PepperoniPizza()
        elif pizzatype == "Vegetarian":
            return VegetarianPizza()
        
factory = PizzaFactory
pizza1 = factory.createpizza("Margherita")
pizza2 = factory.createpizza("Pepperoni")
pizza3 = factory.createpizza("Vegetarian")
pizzas = [pizza1, pizza2, pizza3]

for pizza in pizzas:
    pizza.prepare()


import copy

class StuffedAnimalPrototype:
    def clone(self):
        pass

class Bear(StuffedAnimalPrototype):
    def clone(self):
        return copy.copy(self)
    
class Rabbit(StuffedAnimalPrototype):
    def clone(self):
        return copy.copy(self)
    
class Elephant(StuffedAnimalPrototype):
    def clone(self):
        return copy.copy(self)
    
bearprototype = Bear()
rabbitprototype = Rabbit()
elephantprototype = Elephant()

stuffedanimals = []

for _ in range(5):
    stuffedanimals.append(bearprototype.clone())

for _ in range(3):
    stuffedanimals.append(rabbitprototype.clone())

for _ in range(4):
    stuffedanimals.append(elephantprototype.clone())

for idx, animal in enumerate(stuffedanimals, start = 1):
    print(f"Stuffed Animal {idx}: {animal}")