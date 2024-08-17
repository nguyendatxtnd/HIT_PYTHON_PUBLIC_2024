def so1chuso(a:int):
    if a<10 :
        return True
    else:
        return False
def tongcacchuso(a:int):
    tong = 0
    while a != 0:
        b = a%10
        tong += b
        a = a//10
    return tong
def tongyeucau(a:int):
    if so1chuso(a) == True:
        return a
    else:
        b = tongcacchuso(a)
        if so1chuso(b) == True:
            return b
        else:
            return tongyeucau(b)

n = int(input("nhap so nguyen: "))
print(tongyeucau(n))
