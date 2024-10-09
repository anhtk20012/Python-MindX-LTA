Sum = 0
n = int(input("Nhập vào số nguyên dương: "))
print(f"Tổng các số chẵn từ {1} đến {n} là:", end=" ")
for i in range(1,n+1):
    if i % 2 == 0:
        print(i, end= " ")