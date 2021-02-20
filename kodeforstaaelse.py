#1. Dette er ikke en lovlig kode. Fordi variablen b har endret fra teskstverdi til tallsverdi ved bruk av int(), men linje 5 prøvde å kombinderer et heltall (b) og tekst "Hei!". Ettersom int og str er ikke av samme type og kan da ikke settes sammen.
#2. Vi får feilmelding fordi vi prøver å slå sammen en tesktstreng og et heltall. Hvis vi endrer dette til print(str(b) + "Hei!") gir vi en ny verdi til b nå som er string og kode vil nå fungere.
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")
