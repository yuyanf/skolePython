#Programmet konverterer en txt fil til en liste og regner ut gjennomsnittet av verdiene i lista

minFil = open("temperatur.txt") #Det funker uten "r", må jeg ha med "r" etter "temperatur.txt" her?

listTemperatur = []

for linje in minFil:
    listTemperatur.append(int(linje)) #endrer type til int ellers er linjeskift-\n med.

print(listTemperatur)


def regning(liste):
    summen = 0
    for i in liste:
        summen += i #sett summen til 0 først, og deretter pluss med hver verdi i lista.
    gjennomsnitt = summen/len(liste) #gjennomsnittet er da summen dele på antall, altså lengde av lista
    return gjennomsnitt



resultat = regning(listTemperatur)
print(resultat)
