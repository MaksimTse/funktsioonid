from math import *
from random import *
from tkinter import Pack
#1.
#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
#print("Puu läbimõõdu arvutamine")
#try:
#    C=float(input("Anna ümbermõõt: "))
#    if C>0:
#        d=round(C/pi,2)
#        print("Puu läbimõõt =",d)
#    else:
#        print("C peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale!")

#2.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
#print("Ristkülikukujulise maatüki diagonaal")
#try:
#    N=float(input("Anna pikkus1: "))
#    M=float(input("Anna pikkus2: "))
#    if N>0 and M>0:
#        A=round(sqrt(N**2+M**2),2)
#        print("Ristkülikukujulise maatüki diagonaal =",A)
#    else:
#        print("M ja N peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale!")

#3.
# järgnevast näiteprogrammist semantiline viga:
#try:
#    aeg = float(input("Mitu tundi kulus sõiduks? "))
#    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#    if aeg>0 and teepikkus>0:
#        kiirus = teepikkus / aeg
#        print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    else:
#        print("aeg ja teepikkus peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale!")
#4.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
#print("aritmeetiline keskmine")
#try:
#    A1=int(input("Esimene arv: "))
#    A2=int(input("Teine arv: "))
#    A3=int(input("Kolmas arv: "))
#    A4=int(input("Neljas arv: "))
#    A5=int(input("Viies arv: "))
#    if A1>0 and A2>0 and A3>0 and A4>0 and A5>0:
#        Ak=(A1+A2+A3+A4+A5)/5
#        print("aritmeetiline keskmine =",Ak)
#    else:
#        print("andmed peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale!")

#5.
#Joonista samasugune konn
#print("    @..@")
#print("   (----)")
#print("  ( \__/ )")
#print('  ^^ "" ^^  ')

#6.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
#print("Arvutame kolmnurga ümbermõõdu")
#try:
#    a=randint(0,150)
#    b=randint(0,150)
#    c=randint(0,150)
#    print(f"a={a} \nb={b}\nc={c}")
#    P=round(a+b+c,2)
#    print("Ümbermõõt =",P)
#except:
#    print("Andmetüüp on vale!")
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
#try:
#    l=float(input("Kütuse liitrid kogus: "))
#    km=float(input("Läbitud kilomeetrid: "))
#    if l>0 and km>0:
#        kulu=round((l/km)*100,2)
#        print(f"kütsekulu {kulu}")
#    else:
#        print("andmed peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale!")

#9.
#Rulluisutajad

    #Rulluisutaja keskmine kiirus on 29,9km/h
    #Kui kaugele jõuab M minutiga

#print("Rulluisutajad")
#try:
#    M=int(input("Minutid: "))
#    M=M/60
#    if M>0:
#        tee=round(M*29.9,2)
#        print(f"Jõuab {tee} km")
#    else:
#        print("andmed peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale!")
#10.
#Ajateisendus

    #Kasutaja sisestab aja minutites
    #Sinu valem leiab ja väljastab tunnid ja minutid
    #Näiteks: sisestus 72, vastus 1:12

#print("Ajateisendus")
#try:
#    M=int(input("Sisets aja minutites: "))
#    if M>0:
#        H=M//60 #hours
#        M=M%60 #minutes
#        print(f"vastus {H}:{M}")
#    else:
#        print("andmed peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale!")

#11.
#print (a.isalpha(), a.isdigit()) - proverka vvedeni cifri ili slova
#print("Ema roobot")
#while True:
#    try:
#        a=int(input("Mis hinde sa koolis said?"))
#        if a==5:
#            print("Tubli poiss!")
#        elif a==4:
#            print("Hea poiss!")
#        elif a==3:
#            print("Pole hullu")
#        elif a==2:
#            print("sa pead proovima")
#        else:
#            print("no sa oled loll")
#    except:
#        print("Andmetüüp on vale või sa valesti vastas!")
