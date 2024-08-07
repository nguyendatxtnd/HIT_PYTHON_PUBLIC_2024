dict_1 = {"20221":3.0,
          "20222":2.5,
          "20223":1.8,
          "20224":3.6,
          "20225":2.1,
          "20226":1.5,
          "20227":2.8}
print(dict_1)
a = 0
for key in dict_1.keys():
    if dict_1[key] >= 3.0 and dict_1[key] <= 3.5:
        a += 1
print(f"có {a} sinh viên có điểm tổng kết trong đoạn [3.0, 3.5]")
print("\n")

dict_1["20229"] = 2.6
print("dict sau khi bổ sung thêm 1 sinh viên vào từ điển",dict_1)
print("\n")

key_del = [key for key in dict_1.keys() if dict_1[key] < 2]
for key in key_del:
    del dict_1[key]
print("dict sau khi Xóa mọi sinh viên có điểm tổng kết nhỏ hơn 2.0 ra khỏi từ điển: \n",dict_1)
print("\n")
