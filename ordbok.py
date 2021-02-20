#Programmet ber brukere legge inn to nøkkelverdier og innholdsverdier og printer ut innholdet i ordboka som er både nøkkelverdier og innholdsverdier
varer = {
"melk": 14.90,
"brød": 24.90,
"yoghurt": 12.90,
"pizza": 39.90
}
print(varer)

x = range(2) #for kjører 2 ganger
for n in x:
    vare = input("Oppgi varenavn: ")
    pris = input("Oppgi pris i flyttall: ")
    varer[vare]=pris
print(varer)
