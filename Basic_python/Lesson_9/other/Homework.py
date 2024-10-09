n = int(input("Tổng số bài kiểm tra: "))
List_score = []
count = 0
for i in range(n):
    new_input = float(input("Điểm bài kiểm tra: "))
    List_score.append(new_input)

List_score.sort()

temp_min = List_score[0]
for i in range(n):
    if temp_min > List_score[i]:
        temp_min = List_score[i]
while temp_min in List_score:
    List_score.remove(temp_min)
    
print(List_score)

for i in range(len(List_score)):
    if List_score[i] > 8:
        count = count + 1

print(count)