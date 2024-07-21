import sys

a = int(input("a = "))
if a < 0:
    pass
elif a == 0:
    print(f"can 0 de bieu dien 0 o so nhi phan")
else:
    b = a
    bits = 0
    while a != 0:
        a = a>>1
        bits = bits + 1
    print(f"can {bits} de bieu dien {b} o so nhi phan")

x = "awesome"
print("Python is",x)
print(f"Python is {x}")
print("Python is %s"%(x))

version = sys.version
print(f"version của python hiện tại la: {version}")

