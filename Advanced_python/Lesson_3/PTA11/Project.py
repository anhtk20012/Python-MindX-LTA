# Define the Car class with the __init__() method
class Car:
    def __init__(self, brand: str, color: str, cost: int) -> None:
        self.brand = brand
        self.color = color
        self.cost = cost

# Create an instance of the Car class with specific parameters
Car1 = Car("Toyota", "Red", "1000000")
print(f"Brand: {Car1.brand}")
print(f"Color: {Car1.color}")
print(f"Cost: {Car1.cost}")

print("----------0o0----------")

# Define the Car class with the __init__() method and an additional method to display details
class Car:
    def __init__(self, brand: str, color: str, cost: int) -> None:
        self.brand = brand
        self.color = color
        self.cost = cost

    # Method to display car details
    def show(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Cost: {self.cost}")
        
# Create an instance of the Car class with specific parameters and display its details
Car1 = Car("Toyota", "Red", "1000000")
Car1.show("hihi")

print("----------0o0----------")

# Define the Car class with the __init__() method and an additional method to display details
class Car:
    def __init__(self, brand: str, color: str, cost: int) -> None:
        self.brand = brand
        self.color = color
        self.cost = cost

    # Method to display car details
    def show(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Cost: {self.cost}")
    
    # Method to change the brand of the car 
    def change_brand(self, brand: str):
        self.brand = brand
        
# Create an instance of the Car class and demonstrate the change_brand method
Car1 = Car("Toyota", "Red", "1000000")
print("----------Before----------")
Car1.show()

# Change the brand of the car and display the updated details
print("----------After----------")
Car1.change_brand("Honda")
Car1.show()

print("----------0o0----------")

# Define the base class Car
class Car:
    def __init__(self, brand: str, color: str, cost: int) -> None:
        self.brand = brand
        self.color = color
        self.cost = cost

# Define a derived class called ElectricCar that inherits from Car
class ElectricCar(Car):
    def __init__(self, brand: str, color: str, cost: int, battery_capacity: int) -> None:
        # Call the constructor of the base class Car
        super().__init__(brand, color, cost)
        self.battery_capacity = battery_capacity  # Additional attribute for ElectricCar

    # Method to display the details of the electric car
    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Cost: {self.cost}")
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Create an instance of the derived class ElectricCar
ecar = ElectricCar("Tesla", "Blue", 50000, 75)
ecar.show_details()
