class Dog:
    def __init__(self, Name: str, Breed: str, Color: str, Weight: float) -> None:
        self.name = Name
        self.breed = Breed
        self.color = Color
        self.weight = Weight

class ServiceDog(Dog):
    def __init__(self, Name: str, Breed: str, Color: str, Weight: float, service_type: str) -> None:
        super().__init__(Name, Breed, Color, Weight)
        self.service_type = service_type
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight} kg")
        print(f"Service Type: {self.service_type}")

List_dog = []
for i in range(3):        
    name, breed, color, weight, service_type = input("Enter the name, breed, color, weight and service_type separated by spaces: ").split()
    List_dog.append(ServiceDog(name, breed, color, float(weight), service_type))

for dog in List_dog:
    print("----------0o0----------")
    dog.show_details()