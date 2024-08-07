dict_1 = {"n":1500,
         "m":2,
         "CLUSTERS":3,
         "ITER":10000,
         "METHOD":"FCM",
         "MEASURE":"EUCLIDEAN",
         "YEARS":51}
dict_1["MEASURE"]="MANHATAN"
dict_1["LOSS FUNCTION"]="NORM_2"
dict_1.pop("YEARS")
set_1 = []
s = input("S: ")
for value in dict_1.items():
    set_1.append(value[1])
    if s == str(value[1]):
        print("YES")
set_1 =set(set_1)
l = list(dict_1)
print(dict_1)
print(l)
print(set_1)