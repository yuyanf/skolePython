#Programmet ber brukere taster inn tall og regner ut ifra det ved bruk av fire funksjoner

def addisjon(tall1,tall2):  #definer funksjon addisjon
    summen = tall1 + tall2
    return summen

regning = addisjon(3,9)
print(regning)





def subtraksjon(tall1,tall2):  #definer funksjon subtraksjon
    svar1 = tall1 - tall2
    return svar1

resultat1 = subtraksjon(9,11)
resultat2 = subtraksjon(-2,-19)
resultat3 = subtraksjon(-3,29)

assert resultat1 == -2   #bruk assert ved å sjekke om resultat er riktig. Ingenting skjer dersom det er riktig. Dersom det er feil, er asserterror skrevet ut til terminalen.
assert resultat2 == 17
assert resultat3 == -32






def divisjon(tall1,tall2): #definer funksjon divisjon
    svar2 = tall1/tall2
    return svar2

resultat4 = divisjon(27,9)
resultat5 = divisjon(-24,-2)
resultat6 = divisjon(-18,3)

assert resultat4 == 3
assert resultat5 == 12
assert resultat6 == -6





def tommerTilCm(antallTommer): #definer funksjon tommerTilcm
    assert antallTommer > 0  #parameteren må ha verdi større enn 0 ellers stopper programmet og viser asserterror
    cm = antallTommer*2.54
    return cm

centimeter = tommerTilCm(6)
print(centimeter)






def skrivBeregninger(): #opprett en prosedyre
    print("\nUtregninger:")
    utregning1 = float(input("Skriv inn tall 1: "))  #konverter input fra brukere til flytttall
    utregning2 = float(input("Skriv inn tall 2: "))

    print()
    resultatEn = str(addisjon(utregning1, utregning2)) #sett flytttall inni funksjonene og konverter resultat til streng
    resultatTo = str(subtraksjon(utregning1, utregning2))
    resultatTre = str(divisjon(utregning1, utregning2))

    print("Resultat av summering: " + resultatEn)
    print("Resultat av subtraksjon: " + resultatTo)
    print("Resultat av divisjon: " + resultatTre)


    print("\nKonvertering fra tommer til cm:")
    utregning3 = float(input("Skriv inn et tall: ")) #dersom brukere taster inn mindre enn 0, stopper programmet

    if utregning3 < 0: #bruk if-sjekk til å sjekke om tallet fra brukere er større enn 0, hvis ikke kan de få lov å taste inn igjen.
        utregning3 = float(input("Tallet må være større enn 0: "))
        resultatFire = str(tommerTilCm(utregning3))
        print("Resultat: " + resultatFire)

    else:
        resultatFem = str(tommerTilCm(utregning3))
        print("Resultat: " + resultatFem)



skrivBeregninger()
