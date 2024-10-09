"""
a = 1 --> input
b = 10 --> input
1,2,3,4,5,6,7,8,9 --> range(b)
2+4+6+8 --> if a % 2 == 0, range(a,b,2)
20 --> print 
"""

a = int(input("Nhap so a = "))
b = int(input("Nhap so b = "))
sum = 0
if a % 2 == 1:
    a += 1
for i in range(a,b,2):
    sum += i
print(sum)