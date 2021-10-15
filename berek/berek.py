f = open("berek2020.txt", "r", encoding = "UTF-8")
lista = []
for sor in f:
    lista.append(sor.strip().split(";"))
lista.remove(lista[0])
f.close()
#3.feladat: Dolgozók száma:
print(f"3.feladat: Dolgozók száma: {len(lista)} FŐ")
#4.feladat:bérek átlaga
p2v = lambda x: x.replace(".", ",")
berek = []
for sor in lista:
    berek.append(int(sor[-1]))
atlag = f"{sum(berek) / len(lista) / 1000:.1f}"
print(f"{p2v(atlag)}")
#5.feladat.
reszleg = input("Kérem egy részleg nevét: ")
nincs = "A megadott részleg nem létezik a cégnél"

xxx = max( [ (int(sor[-1]),sor )for sor in lista if reszleg in sor])




print(f"    Név:{xxx[1][0]}")
print(f"    Neme:{xxx[1][1]}")
print(f"    Belépés:{xxx[1][3]}")
print(f"    bér:{xxx[0]} Forint")
