class Dog:
    def __init__(self, Name: str, Breed: str, Color: str, Weight: float) -> None:
        self.name = Name
        self.breed = Breed
        self.color = Color
        self.weight = Weight

List_dog = []
for i in range(3):        
    name, breed, color, weight = input("Enter the name, breed, color, and weight separated by spaces: ").split()
    List_dog.append(Dog(name, breed, color, float(weight)))

for i in range(3):
    print("----------0o0----------")
    print(f"Name: {List_dog[i].name}")
    print(f"Breed: {List_dog[i].breed}")
    print(f"Color: {List_dog[i].color}")
    print(f"Weight: {List_dog[i].weight} kg")
    