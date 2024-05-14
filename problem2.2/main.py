def faktor_bilangan(bilangan):
    m = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            m.append(i)
    return m

bilangan = int(input("Masukkan nilai = "))  
m = faktor_bilangan(bilangan)  
m.sort(reverse=True)  # mengurutkan m secara descending
for factor in m:
    print(factor)   
