n =int(input("n = "))
l = []
a = 0
for i in range(1,n+1):
    tong_1 = 0
    for j in range(1,i):
        if i % j == 0:
            tong_1 += j
    if i == tong_1:
        l.append(i)
        a += 1
if a==0:
    print(f"khong co so hoan thien trong doan [1, {n}]")
else:
    print(f"cac so hoan thien trong doan [1, {n}]: ")
    for i in range(0,a):
        print(l[i], end = ", ")



