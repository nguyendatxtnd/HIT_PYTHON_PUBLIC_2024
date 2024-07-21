
#Tính tổng các chữ số trong một số nguyên dương
print("Tính tổng các chữ số trong một số nguyên dương")
a = int(input("nhap so nguyen duong: "))
d = a
tong = 0
while d != 0:
    b = d%10
    tong += b
    d = d//10
print("tong cac so trong so ",a," la: ",tong)

#Tính tổng các ước số của một số nguyên dương
print("\nTính tổng các ước số của một số nguyên dương")
n = int(input("nhap so nguyen duong n = "))
tong_uoc = 0
for i in range(1,n+1):
    if n % i == 0:
        tong_uoc += i
print("tong cac uoc so cua so nguyen duong ",n," la: ",tong_uoc)

#Kiểm tra tam giác
print("\nKiểm tra tam giác")
print("nhap 3 so nguyen duong: ")
n_1 = int(input("nhap so nguyen duong 1: "))
n_2 = int(input("nhap so nguyen duong 2: "))
n_3 = int(input("nhap so nguyen duong 3: "))

if n_1 + n_2 > n_3 and n_3 + n_2 > n_1 and n_1 + n_3 > n_2:
    print("3 so tren co the tao thanh tam giac")
    if n_1 == n_2 == n_3:
        print("do la 1 tam giac deu")
    elif n_1 == n_2 or n_2 == n_3 or n_1 == n_3:
        if n_1**2 + n_2**2 == n_3**2 or n_2**2 + n_3**2 == n_1**2 or n_1**2 + n_3**2 == n_2**2:
            print("do la 1 tam giac vuong can")
        else:
            print("do la 1 tam giac can")
    elif n_1**2 + n_2**2 == n_3**2 or n_2**2 + n_3**2 == n_1**2 or n_1**2 + n_3**2 == n_2**2:
        print("do la 1 tam giac vuong")
    elif n_1**2 + n_2**2 < n_3**2 or n_2**2 + n_3**2 < n_1**2 or n_1**2 + n_3**2 < n_2**2:
        print("do la mot tam giac tu")
    elif n_1**2 + n_2**2 > n_3**2 and n_2**2 + n_3**2 > n_1**2 and n_1**2 + n_3**2 > n_2**2:
        print("do la mot tam giac nhon")
else:
    print("3 so tren khong the tao thanh tam giac")
    





















