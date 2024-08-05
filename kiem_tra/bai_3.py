n = int(input("nhập số lượng sinh viên tham gia kiểm tra: "))

name = []
point = []
for i in range(0,n):
    ten = str(input("nhap ten: "))
    name.append(ten)
    diem = float(input("nhap diem: "))
    point.append(diem)

diem_min = point[0]
for i in point:
    if i < diem_min:
        diem_min = i
print("sinh vien co diem thap nhat: ")
for i in range(0,n):
    if point[i] == diem_min:
        print(f"{name[i]} : {point[i]} điểm")
    
