#Programmet skriver ut matplan for den oppgitte personen
liste1 = ["Kornfleks", "Salat", "Eple"]
liste2 = ["Kaffe", "Lasagne", "Mcdonald"]
liste3 = ["Brødskiver", "Kyllingsuppe", "Spaghetti Bolognese"]

sykehjem = {
    "Ludo Mohammed": liste1,
    "Luna Nordmann": liste2,
    "Anton Do": liste3
}

def prosedyre():
    print("Hei! \nLudo Mohammed, Luna Nordmann og Anton Do bor her. Skriv det navnet du ønsker å se matplanen for:")
    navn=input()
    if navn in sykehjem:
        print(sykehjem[navn])
    else:
        print("Denne person fins ikke!")

prosedyre()

# a skal ha mengde fordi brukernavn er alltid unik
# b skal ha ordbok fordi det skal være en nøkkelverdi som er brukernavn(alltid unik) og en innholdsverdi som er poeng tilhørerende hver student, og disse kan ha like verdier.
# c skal ha liste fordi navn kan være likt
# Hvis det er en felles meny for alle, da skal d ha mengde for å luke ut samme allergener gjestene har. Dersom hver gjest skal få sin meny, burde det bruke ordbok.
