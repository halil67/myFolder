import random

def sayi_uret(n):
    return [random.randint(1, 10) for _ in range(n)]


while True:
    n=random.randint(1,10)
    sayi=sayi_uret(n)
    sayi_str = "".join(str(num) for num in sayi)
    print(sayi_str)
    s=random.randint(1,9)
    if str(s) in sayi_str:
        print(s,"var")
        print(sayi_str.index(str(s)))
    else:
        print("yok",s)
    break