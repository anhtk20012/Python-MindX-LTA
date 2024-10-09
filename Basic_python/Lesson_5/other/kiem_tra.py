# lg = int(input('Loại giấy tờ: ')) # --> str --> int
# st = int(input('Số trang: '))
# if lg == 1:
#     print(f'Số lượng giấy cần dùng: {st}')
# else:
#     print(f'Số lượng giấy cần dùng: {st//2 + st%2}')

d = int(input("Nhập số kWh tiêu thụ: "))
t = 0
if d > 50:
    t = t + 50 * 1700
    if d > 100:
        t = t + 50 * 1900
        if d > 200:
            t = t + 100 * 2100 + (d-200) * 3000
        else:
            t = t + (d-100) * 2100
    else:
        t = t + (d-50) * 1900
else:
    t = t + d * 1700

print(f"Số tiền điện cần phải trả: {t} đồng")

if d <= 50:
    t = d * 1700
elif 51 <= d <= 100:
    t = 50 * 1700 + (d-50) * 1900
elif 101 <= d <= 200:
    t = 50 * 1700 + 50 * 1900 + (d-100) * 2100
else:
    t = 50 * 1700 + 50 * 1900 + 100 * 2100 + (d-200) * 3000