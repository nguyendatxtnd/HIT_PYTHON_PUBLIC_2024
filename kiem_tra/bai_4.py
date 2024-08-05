n = int(input("nhap so luong phan tu trong list: "))
l = []
for i in range(0,n):
    s = str(input())
    l.append(s)

l_2 = []

for i in l:
    for j in range(0, len(i)):
            l_2.append(i[j])

l_2 = set(l_2)
l_2 = list(l_2)
print(l_2)


            
