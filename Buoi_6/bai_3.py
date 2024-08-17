
def calculate(s:str, *args):
    if s == "add":
        l = list(args)
        return sum(args)
    elif s == "multiply":
        mul = 1
        for i in args:
            mul *= i
            return mul
    elif s == "max":
        return max(args)
    elif s == "min":
        return min(args)
    else:
        return "Invalid operation"


s = str(input("operation: "))

print(calculate(s,1,2,3,4,5,6,7,8,9))