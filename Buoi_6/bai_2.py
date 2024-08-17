import numpy as np

def matrix_transpose(a:np.array):
    mt = np.transpose(a)
    return mt

def matrix_input():
    n = int(input("nhap so hang: "))
    m = int(input("nhap so cot: "))
    l_n = []
    for i in range(0,n):
        l_m = []
        for j in range(0,m):
            a = int(input(f"mt[{i}][{j}] = "))
            l_m.append(a)
        l_n.append(l_m)
    mt = np.array(l_n)
    return mt

mt = matrix_input()
mt_transpose =  matrix_transpose(mt)
print("matrix origin: \n",mt)
print("matrix transpose: \n",mt_transpose)


