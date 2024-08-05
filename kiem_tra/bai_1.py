n = int(input("nhap so luong phan tu: "))
l = []
for i in range(0,n):
    a = int(input())
    l.append(a)

l = tuple(l)

l_so = []
l_dem = []
for i in range(0,10000):
    l_dem.append(0)
for i in l:
    if l_dem[i] == 0:
        l_so.append(i)
    l_dem[i] += 1

for i in l_so:
    if l_dem[i] % 5 == 0 and l_dem[i] %10 != 0:
        print(i)
        



        



