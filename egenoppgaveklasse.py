#Skriv en klasse Person med en konstruktør som tar imot navn og alder. I tillegg skal konstruktøren ha en tom liste hobbyer. Skriv en metode leggTilHobby som tar imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje. Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et Person-objekt med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal statistikk om brukeren skrives ut.



class Person:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.hobbyer = []


    def leggTilHobby(self):
        print("\nHva er din hobby? Venligst tast inn din hobby. Skriv ''Ferdig'' dersom du ikke ønsker å fortsette.")
        tekst = 0 #sett tekst til verdi 0 først
        while tekst != "Ferdig": #når tekst ikke har verdig "Ferdig" vil while-løkka alltid loope
            tekst = input("Din hobby: ")

            if tekst != "Ferdig": #hvis tekst ikke har verdig "Ferdig"
                self.hobbyer.append(tekst) #tekst sine verdier settes i lista


    def skrivHobbyer(self):
        ord = "" #sett variablen ord til string først

        for i in self.hobbyer:
            ord = ord + i + ", " #for hver element i lista, putt den inni variablen ord og legger til ", ".

        print("Dine hobbyer er:\n"+ ord[0:-2]) #posisjoner sier at kun ord sin første verdi til andre siste verdi blir med. Dette er for å fjerne siste ", ".



    def skrivUt(self):

        print("\nHei,", self.navn+"!", "Du er", self.alder,"år gammel.")
        self.skrivHobbyer() #skriv ut navn, alder og hobbyer
        print()




etNavn = input("Hva heter du?\n")
enAlder = input("\nHvor gammel er du?\n")


dennePerson = Person(etNavn, enAlder)
dennePerson.leggTilHobby()
dennePerson.skrivUt()
