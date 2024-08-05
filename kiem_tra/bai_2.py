x = int(input("nhap toa do diem dich x: "))
while x<1 or x>1000:
    print("nhap lai: ")
    x = int(input("nhap toa do x: "))

a = x//3 
b = x%3
if b == 0:
    print(f"số bước tối thiểu rùa cần đi là: {a}")
else:
    print(f"số bước tối thiểu rùa cần đi là: {a+1}")
