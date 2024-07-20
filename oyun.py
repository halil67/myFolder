import random

def sayi_uret(n):
    return [str(random.randint(1, 9)) for _ in range(n)]


while True:
    n=random.randint(2,10)
    sayi=sayi_uret(n)
    sayi_str = "".join(str(num) for num in sayi)
    
    while True:
        snc=[]
        tahmin=input(f"sayımız {n} basamaklıdır.\n Tahminiz nedir?")
        
        for s in list(tahmin):
            if s in sayi:
                if sayi.index(s)==tahmin.index(s):
                    snc.append(s + "+")
                else:
                    snc.append(s+"-")
        print(snc)                  
        if tahmin==sayi_str:
            print("TEBRLER")
            
            break
        else:
            continue
        
    print(sayi_str)
    break
    
