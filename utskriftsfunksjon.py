#Programmet skal stille samme spørsmål 3 ganger og skriver ut det brukere har svart til terminalen
def utskrift(): #først lager jeg en vanlig input-funksjon kode og gir kode navn som utskrift. siden det brukere skriver inn er tekst, så jeg kan bare legger til utropstegn og punktum ved slutten av input
    navn = input("Skriv inn navn: ")+"!"
    bosted = input("Hvor kommer du fra? ")+"."
    print("Hei,",navn,"Du er fra",bosted)
def linjeskift():#navngi kode 2 som linjeskif siden denne er for linjeskift
    print()

utskrift() #nå kjører jeg prosedyren 3 ganger ved å kun skriver navn til kode1 og 2. Her er det viktig å fjerne kolon.
linjeskift()
utskrift()
linjeskift()
utskrift()
