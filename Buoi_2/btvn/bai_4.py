n = int(input("nhap so luong so Fibonaccin = "))
l = []

if n == 1:
    l.append(0)
elif n == 2:
    l.append(0)
    l.append(1)
else:
    l.append(0)
    l.append(1)
    for i in range(2,n):
        a = l[i-2] + l[i-1]
        l.append(a)
for i in range(0,len(l)):
    print(l[i],end=", ")



        



