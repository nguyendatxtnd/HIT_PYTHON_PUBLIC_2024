def lambda_expression(a:str, b:str):
    l = []
    l.append(a)
    l.append(b)
    l = set(l)
    l = list(l)
    return l[0]

a = lambda_expression("b","a")

print(a)
