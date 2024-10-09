An = int(input("Chiều cao của An: "))
Minh = int(input("Chiều cao của Minh: "))
Lan = int(input("Chiều cao của Lan: "))

if An >= Minh and An >= Lan:
    print("An cao nhất.")
elif Minh >= An and Minh >= Lan:
    print("Minh cao nhất.")
else:
    print("Lan cao nhất.")