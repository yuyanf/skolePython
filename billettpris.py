#Programmet ber brukere skrive inn en alder 4 ganger og beregner hvor mye de må betale for hver alder.
def prosedyre():
    alder = int(input("Oppgi en alder: "))
    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder > 17 and alder < 63:
        billettpris = 50
    else:
        billettpris = 35

    print("Du må betale:", billettpris)

x = range(4)
for n in x:
    prosedyre()
#Dersom brukere skriver inn en tesktstreng eller ikke heltallsverdi- noe som ikke er int() vil det skape problemer. Fordi if-sjekk min baserer på at input skal være en int()
