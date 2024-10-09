# Define the Dog class with default attributes
class Dog:
    name = ""
    breed = ""
    color = ""
    weight = 0
    
# Create an instance of the Dog class for Bo
Bo = Dog()
print(Bo)
print(type(Bo))

print("----------0o0----------")

# Set the name and breed attributes for the Bo object
Bo.name = "Bo"
Bo.breed = "Alaska"
print(f"Name: {Bo.name}\nBreed: {Bo.breed}")

print("----------0o0----------")

# Define the Car class with the __init__() method to initialize attributes
class Car:
    def __init__(self, brand: str, color: str, cost: int) -> None:
        self.brand = brand
        self.color = color
        self.cost = cost

# Create an instance of the Car class with specific parameters
Car1 = Car("Toyota", "Red", 1000000)
print(f"Brand: {Car1.brand}")
print(f"Color: {Car1.color}")
print(f"Cost: {Car1.cost}")
