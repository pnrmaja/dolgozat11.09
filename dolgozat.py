import math
import random


def feladat1():
    szam= int(input("Kérek egy páros számot"))
    while (szam %2 !=0):
        if (szam % 2 == 0):
            print(f"A szám páros {szam}")
        else:
            szam = int(input("Ez nem páros páros számot kérek"))



def feladat2():
    i: int=0


    while (i<13):
        szam=math.floor(random.random()*(151-10)+10)
        print(szam, end=" ")
        i=i+1
        if (szam%3==0):
            print(f"Ez a szám osztahtó 3-mal: {szam}")

def feladat3(text,N):
    szoveg: str=text
    szam: int = N
    if (text < 0):
        print("Nincs N. karakter!")
    else:
        print(len(N))

def felafat4():
    db = 0
    nev = input("Kérek egy nevet")
    while (nev != "@"):
        db = db + 1
        nev = input("Kérek egy nevet")
    if(nev=="@"):
            print(f"A felhasználó {db} nevet adott meg.")

def feladat5():
    bekeres=input("Kérek egy tippet kő/papír/olló")
    felhasznalo_tippje=bekeres
    kő=1
    papír=2
    olló=3
    gep_tippje=kő,papír,olló
    i : int=1
    while (i<3):
        szam = math.floor(random.random()*3)
        if (felhasznalo_tippje>gep_tippje):
            print("A felhasználó nyert")
        elif (felhasznalo_tippje<gep_tippje):
            print("A gép nyert")
        else:
            print("Döntetlen")

        i=i+1















