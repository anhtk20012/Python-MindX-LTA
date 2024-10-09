print("Số tiền chi tiêu trong tuần (Đơn vị: Nghìn đồng):")
week = []
for i in range(6):
    day = int(input())
    week.append(day)
    
sum = 0
for i in range(len(week)):
    sum += week[i]
print(f"Tổng chi tiêu: {sum}")

number_max = max(week)
name_day = []
for i in range(len(week)):
    if number_max == week[i]:
        name_day.append(f"Thứ {i+2}")
print("Ngày chi tiền nhiều nhất:", end = " ")
for i in range(len(name_day) - 1):
    print(name_day[i], end=", ")
print(name_day[len(name_day) - 1])

print(f"Trung bình chi tiêu của mỗi ngày trong tuần: {round(sum/6, 1)}")