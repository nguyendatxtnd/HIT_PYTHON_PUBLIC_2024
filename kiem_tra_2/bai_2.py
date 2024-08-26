def sohoanhao(a:int):
    b = a
    t = 0
    while b != 0:
        c = b % 10
        t += c
        b = b//10
    if t == 10:
        return True
    else:
        return False

a = int(input("stt: "))

b = 0
c = 0
while b != a:
    c += 1
    while 1:
        if sohoanhao(c) == True:
            break
        else:
            c += 1
    b += 1
print(c)
    
    