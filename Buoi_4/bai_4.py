from itertools import combinations

set_1 = set()
set_2 = set()

n = int(input("nhap so phan tu cua set n = "))
for i in range(0,n):
    a = int(input(f"phan tu {i}: "))
    set_1.add(a)

tong_gioi_han = int(input("nhap so nguyen: "))

tong_max = 0
for i in range(1,n+1):
    for set_con in combinations(set_1,i):
        tong_set_con = sum(set_con)
        if tong_set_con <= tong_gioi_han and tong_set_con > tong_max:
            tong_max = tong_set_con
            set_2 = set(set_con)

print(f"set chứa các phần tử của tập hợp con lớn nhất thỏa mãn điều kiện tong set <= {tong_gioi_han}",set_2)









