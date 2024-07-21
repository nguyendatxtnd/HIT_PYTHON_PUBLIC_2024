
n = 100
#S(n) = 1 - 2 + 3 - 4 + 5 + .... + (2*n + 1)
tong = 0
for i in range(1,(2*n+1)+1):
    if i % 2 != 0:
        tong += i
    else:
        tong -= i
print("S(",n,") = 1 - 2 + 3 - 4 + 5 + .... + (2*",n," + 1) = ",tong)

#S(n) = 1 + ½ + ⅓ + ¼ +.....+1/n
tong_2 = 0
for i in range(1,n+1):
    tong_2 += 1/i
print("S(",n,") = 1 + ½ + ⅓ + ¼ +.....+1/",n," = ",tong_2)

#Biện luận nghiệm của phương trình bậc 2 một ẩn
import math
a = 1
b = -3
c = 2
delta = b**2 - 4*a*c   
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có hai nghiệm phân biệt: x1 = ",x1," x2 = ",x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có một nghiệm kép: x = ",x)
else:
    print("Phương trình vô nghiệm")


        
    
