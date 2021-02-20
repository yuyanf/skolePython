#Programmet har to funksjoner, den ene regner ut summen av to heltall, og den andre teller hvor mange ganger en bokstav brukere taster inn forekommer i teksten som også skrevet av brukere.

def adder (tall1, tall2):
    sum = tall1 + tall2
    return sum  #Jeg lager funksjon adder som har to parametre. funksjonen skal regne ut summen av to parametre og retunere summen.

resultat1 = adder (7,13)
resultat2 = adder (4,20)  #funksjonen har fått seg to heltall som parametere og blir putta i to variabler

print("Summen blir da " + str (resultat1))
print("Summen blir da " + str (resultat2)) #nå kan jeg skrive ut resultat

"""
svar1 = input("Skriv en setning: ")
svar2 = input("Skriv en bokstav: ")
mylist = list(svar1)
x = mylist.count(svar2)
print(x)
"""


def tellForekomst(minTekst, minBokstav):
    mylist = list(minTekst)
    x = mylist.count(minBokstav)
    return x   #Funksjonen tellForekost har to parametre, den ene skal bli splittet opp til enkle bokstaver og blir en liste, count metode skal telle hvor mange den andre parameter finns i denne lista

svar1 = input("Skriv en setning: ")
svar2 = input("Skriv en bokstav: ")
forekomst = tellForekomst(svar1, svar2)
print(forekomst)
