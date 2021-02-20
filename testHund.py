#Programmet importerer en klasse og oppretter et objekt av klasse. Ved bruk av while-løkke kan brukeren skriver inn hvor mye de vil fore hunden og da blir hundens index skrevet ut til brukeren.

from hund import Hund


def hovedprogram():


    print("Hei og velkommen til Jenny-dyreklinikken. Vennligst tast inn svar etter spørsmål. Du kan når som helst avslutte programmet.")

    svar = 0

    luna = Hund(10, 4, 10) #oppretter objekt av klasse


    while svar != "Ja": #While-løkka er for å la hunden løpe og spise minst 2 ganger til brukeren vil avslutte

        luna.spring()
        luna.printUt()
        hundSpis = input("Hvor mange skjeer for vil du gi hunden: ")
        luna.spis(hundSpis)
        luna.printUt()

        svar = input("Vil du avslutte?(Ja/Nei): ") #



hovedprogram()
