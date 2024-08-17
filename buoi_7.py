# def hello(n:int, s:str):
#     a = str(n) + s
#     return a

# n = 1
# s = "rfeger"
# a = hello(n,s)
# print(a)

# def function_1(number):
#     print(number)
# function_1(1)

# def function_1(*number):
#     print(number)
# function_1(1,2,3,4)

# def function_2(**number):
#     print(number)
# function_2(a = "hey", b = "hello", c = "hi")

# def tinh_tong(n):
#     t = n
#     if n != 0:
#         t += tinh_tong(n-1)
#         return t
#     else:
#         return t
# a  = 5  
# t  = tinh_tong(5)
# print(t)


def fibonaci(a:int):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    return fibonaci(a-1) + fibonaci(a-2)

print(fibonaci(6))


















