import re
m = r"^[a-zA-Z]"

s = str(input("nhap chuoi: "))
c = ""
d = ""
t = 0

for ch in s:
    if re.match(m,ch) == False:
        c += str(ch)
    else:
        c += "_"
for i in c:
    if i != "_":
        d += i
    elif d != "":
        d = int(d)
        t += d
        d = ""
    else:
        pass
print(t)
        
        

