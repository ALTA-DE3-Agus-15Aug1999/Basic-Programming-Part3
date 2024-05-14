def faktor_bilangan(bilangan):
    m = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            m.append(i)
    return m

bilangan = int(input("Masukkan bilangan = "))  
m = faktor_bilangan(bilangan)  
for factor in m:    # mengurutkan
    print(factor)  