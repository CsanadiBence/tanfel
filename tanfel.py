"""
tantargyFelosztas=[]
with open("./beosztas.txt","r",encoding="UTF-8" )as fin:
    for sor in fin:
        tantargyFelosztas.append(sor.strip())
        
for elem in tantargyFelosztas:
    print(f"{elem},")
    
print(f"a listaban {int(len(tantargyFelosztas)/4)} elem van")
"""
tanarok=[]
tantargyak=[]
osztalyok=[]
oraszamok=[]

rekord=[]

with open("./beosztas.txt","r",encoding="UTF-8" )as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len(rekord)==4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszamok.append(int(rekord[3]))
            rekord=[]
for i in range(len(tanarok)):
    print(f"{tanarok[i]}, {tantargyak[i]}, {osztalyok[i]}, {oraszamok[i]}")
    

    
print("2.feladat")
print(f"a bejegyzesek szama: {len(tanarok)}")

print("3.feladat")
print(f"Az iskolában a heti összóraszám: {sum(oraszamok)}")


def összegzés(be_tanar,tanarok,oraszamok):
    összoraszam=0
    for i in range(len(tanarok)):
        if tanarok[i] == be_tanar:
            összoraszam+=oraszamok[i]
    return összoraszam
print("4.feladat")
be_tanar=input("Egy tanár neve= ")
print(f"A tanár heti össz oraszám: {összegzés(be_tanar,tanarok,oraszamok)}")


def eldontes(be_osztaly,be_tantargy,tantargyak,osztalyok):
    i=0
    while (i<len(tantargyak) and not (be_tantargy==tantargyak[i] and be_osztaly.split(".")[0]==osztalyok[i].split(".")[0] and "x" in osztalyok[i])):
        i+=1
    return i<len(tantargyak)
print("6.feladat")
be_osztaly=input("Osztaly: ") or "10.b"
be_tantargy=input("Tantargy: ") or "kémia"

if eldontes(be_osztaly,be_tantargy,tantargyak,osztalyok):
    print("Csoportban Tanulják")
else:
    print("Nem csoportban tanulják.")

tanarnevek=[]
for tanar in tanarok:
    if tanar not in tanarnevek:
        tanarnevek.append(tanar)
    
print("7.feladat")
print(f"Az iskolában: {len(tanarnevek)} tanár tanít")
