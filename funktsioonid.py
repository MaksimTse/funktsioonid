from math import *
from random import *
from tkinter import Pack
#1.
#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
#print("Puu läbimõõdu arvutamine")
#C=float(input("Anna ümbermõõt: "))
#d=round(C/pi,2)
#print("Puu läbimõõt",d)

#2.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
#print("Ristkülikukujulise maatüki diagonaal")
#N=float(input("Anna pikkus1: "))
#M=float(input("Anna pikkus2: "))
#A=round(sqrt(N**2+M**2),2)
#print("Ristkülikukujulise maatüki diagonaal =",A,"m")

#3.
#Leidke järgnevast näiteprogrammist semantiline viga:
#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg
#print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
#print("aritmeetiline keskmine")
#A1=int(input("Esimene arv: "))
#A2=int(input("Teine arv: "))
#A3=int(input("Kolmas arv: "))
#A4=int(input("Neljas arv: "))
#A5=int(input("Viies arv: "))
#Ak=(A1+A2+A3+A4+A5)/5
#print("aritmeetiline keskmine =",Ak)

#5.
#Joonista samasugune konn
#print("    @..@")
#print("   (----)")
#print("  ( \__/ )")
#print('  ^^ "" ^^  ')

#6.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
#print("Arvutame kolmnurga ümbermõõdu")
#a=randint(0,100)
#b=randint(0,100)
#c=randint(0,100)
#print(f"a={a} \nb={b}\nc={c}")
#P=round(a+b+c,2)
#print("Ümbermõõt =",P)

#7.
#Pitsa

    #Võtsite P sõbraga suure pitsa hinnaga 12,90€
    #Jätate teenindajale 10% jootraha
    #Koosta programm, mis leiab kui palju peab igaüks maksma

#print("Pitsa jootraha arvutamine")
#P=randint(1,10)
#Pitsa=12.9
#Jootraha=Pitsa/10
#summa=Jootraha/P
#print(f"{P}-st, Igaüks maksab {summa}")

#8.
#Kütusekulu arvutamine

    #Kasutaja sisestab tangitud kütuse liitrid
    #Kasutaja sisestab läbitud kilomeetrid
    #Programm leiab kütusekulu 100km kohta keskmiselt

#print("Kütusekulu arvutamine")
#l=float(input("Kütuse liitrid kogus: "))
#km=float(input("Läbitud kilomeetrid: "))
#kulu=round((l/km)*100,2)
#print(f"kütsekulu {kulu}")

#9
#Rulluisutajad

    #Rulluisutaja keskmine kiirus on 29,9km/h
    #Kui kaugele jõuab M minutiga

#print("Rulluisutajad")
#M=int(input("Minutid: "))
#M=M/60
#tee=round(M*29.9,2)
#print(f"Jõuab {tee} km")

#10
#Ajateisendus

    #Kasutaja sisestab aja minutites
    #Sinu valem leiab ja väljastab tunnid ja minutid
    #Näiteks: sisestus 72, vastus 1:12

#print("Ajateisendus")
#M=int(input("Sisets aja minutites: "))
#H=M//60 #hours
#M=M%60 #minutes
#print(f"vastus {H}:{M}")