class Tamthucb2:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def khoitaogiatri():
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        return a,b,c
    def __str__(self):
        print(f"{self.a}x2 + ({self.b})x + ({self.c})")
    def cong2tt(self):
        a1,b1,c1 = self.khoitaogiatri()
        a1 = Tamthucb2(a1,b1,c1)
        a2,b2,c2 = self.khoitaogiatri()
        a2 = Tamthucb2(a2,b2,c2)
        a3 = Tamthucb2(a1+a2,b1+b2,c1+c2)
        a3.__str__()
    def hieu2tt(self):
        a1,b1,c1 = self.khoitaogiatri()
        a = Tamthucb2(a1,b1,c1)
        a2,b2,c2 = self.khoitaogiatri()
        a2 = Tamthucb2(a2,b2,c2)
        a3 = Tamthucb2(a1-a2,b1-b2,c1-c2)
        a3.__str__()

print("tam thuc 1: ")
a1 = Tamthucb2
a1,b1,c1 = a1.khoitaogiatri()
a1 = Tamthucb2(a1,b1,c1)
a1.__str__()
print("tam thuc 2: ")
a2 = Tamthucb2
a1,b1,c1 = a2.khoitaogiatri()
a1 = Tamthucb2(a1,b1,c1)
a2.__str__()








        
    