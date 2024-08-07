s = str(input("nhập chuỗi kí tự: "))
l=[]
for i in s:
    l.append(i)

cackitu = set(l)
cackitu = list(cackitu)
demcackitu = []
for i in range(0,len(cackitu)):
    demcackitu.append(0)

for i in range(0,len(cackitu)):
    for j in s:
        if cackitu[i] == j:
            demcackitu[i] += 1
dict_1 = {}
for i in range(0,len(cackitu)):
    dict_1[cackitu[i]] = demcackitu[i]

print(dict_1)
