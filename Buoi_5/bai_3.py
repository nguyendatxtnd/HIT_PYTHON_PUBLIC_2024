import random

n = int(input("nhập số lượng tài khoản sinh viên: "))
while n<10 or n>100000:
    print("nhap lai: ")
    n = int(input("nhập số lượng tài khoản sinh viên: "))
dict_1 = {}
for i in range(0,n):
    print(f"sv{i+1}\n")
    print("nhap MSV: ")
    msv = str(input("MSV : "))
    while len(msv) != 10:
        print("nhap lai msv: ")
        msv = str(input("MSV : "))
    password = random.choice(["CNTT","KHMT", "KTPM", "HTTT"]) + msv
    dict_sv = {"Username":msv,
               "Password":password}
    dict_1[f"account{i+1}"] = dict_sv

print(dict_1)

