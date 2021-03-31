"""
jarjestanumerot_0_2.py, numeroiden järjestämis peli
@author: Benjamin Pörhö
"""
print("Järjestä luvut vaihtamalla niitä tyhjän kanssa")

numerot = ['4', '7', '2', '6', '8', '3', '5', '_', '1']
vertaa = ('1', '2', '3', '4', '5', '6', '7', '8', '_')
print ("Oikea järjestys: ", vertaa)
print("Sekoitetut numerot: ", numerot)
kierros = 0

siirto = input ("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
tyhja = '_'
tyhja_index = numerot.index(tyhja)
siirto_index = numerot.index(siirto)

numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

print (numerot)
#Tiedän, ettei mitään järkeä tehdä kahdeksalla if lauseella, mutta kun ei saanut käyttää looppia,
#niin en keksinyt muuta tapaa.

if numerot != ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    siirto = input("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
    tyhja = '_'
    tyhja_index = numerot.index(tyhja)
    siirto_index = numerot.index(siirto)

    numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

    print(numerot)
if numerot != ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    siirto = input("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
    tyhja = '_'
    tyhja_index = numerot.index(tyhja)
    siirto_index = numerot.index(siirto)

    numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

    print(numerot)
if numerot != ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    siirto = input("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
    tyhja = '_'
    tyhja_index = numerot.index(tyhja)
    siirto_index = numerot.index(siirto)

    numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

    print(numerot)
if numerot != ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    siirto = input("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
    tyhja = '_'
    tyhja_index = numerot.index(tyhja)
    siirto_index = numerot.index(siirto)

    numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

    print(numerot)
if numerot != ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    siirto = input("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
    tyhja = '_'
    tyhja_index = numerot.index(tyhja)
    siirto_index = numerot.index(siirto)

    numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

    print(numerot)
if numerot != ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    siirto = input("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
    tyhja = '_'
    tyhja_index = numerot.index(tyhja)
    siirto_index = numerot.index(siirto)

    numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

    print(numerot)
if numerot != ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    siirto = input("Minkä numeron haluat vaihtaa tyhjän kanssa?: ")
    tyhja = '_'
    tyhja_index = numerot.index(tyhja)
    siirto_index = numerot.index(siirto)

    numerot[tyhja_index], numerot[siirto_index] = numerot[siirto_index], numerot[tyhja_index]

    print(numerot)
if numerot == ['1', '2', '3', '4', '5', '6', '7', '8', '_']:
    print ("Numerot ovat oikeassa järjestyksessä, voitit pelin!")
else:
    print("Siirrot loppuivat, hävisit pelin!")