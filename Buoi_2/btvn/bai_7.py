def tong_uoc(n):
    tong = 0
    for i in range(1,n):
        if n % i == 0:
            tong += i
    return tong

n = int(input("n = "))
l_amicable = []
for i in range(1,n+1):
    a = tong_uoc(i)
    if  a >= 1 and a <= n:
        if tong_uoc(a) == i and a != i:
            l_amicable.append([i,a])
print(f"cac cap so amicable trong doan [0, {n}] la: ")
for i in range(0,len(l_amicable)):
    print(l_amicable[i])


