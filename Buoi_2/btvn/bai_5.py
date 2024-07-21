n = int(input("n = "))
l_1 = []
for i in range(1, n+1):
    a = i  
    l = []
    while i != 0:
        b = i % 10
        l.append(b)
        i = i // 10
    tong_3 = 0
    for j in range(len(l)):
        tong_3 += l[j] ** 3
    if tong_3 == a:
        l_1.append(a)
if len(l_1) == 0:
    print(f"không có số armstrong nào trong đoạn [1, {n}]")
else:
    print(f"các số armstrong trong đoạn [1, {n}]: ")
    for i in l_1:
        print(i, end=", ")
