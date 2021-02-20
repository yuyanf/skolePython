#Programmet leser inn en fil med navn til selgere og antall salg per selger, og regner ut hvem solgte mest, summen av alle salg og gjennomsnitt salg.


def innlesning(filnavn):
    minFil = open(filnavn) #åpen fil
    minList = []
    for linje in minFil:
        biter = linje.split(" ")
        minList.append(biter) #for-løkke lopper gjennom filen. For hver linje skal linja splites etter mellom og bli til en liste. dvs. hver liste består da av navn til selger og antall salg til selger. Lista legger til slutten av minList(som var en tom list til å starte med) ved bruk av append. minList blir da en liste som inneholder mange lister.

    minOrdbok = dict(minList) #konverter minList til en ordbok
    for x in minOrdbok:
        minOrdbok[x] = int(minOrdbok[x]) #for løkke lopper gjennom ordbok. For hver key i ordbok, key sin innholdsverdi blir et heltall
    return minOrdbok






def maanedensSalgsperson(ordbok):
    mest = 0 #sett mest til verdi 0
    navn = "" #sett navn til en streng
    for i in ordbok:
        tall = int(ordbok[i]) #for hver key i ordbok, key sin innholdsverdi blir et heltall og settes inni variabel tall
        if tall > mest: #hvis tall (key sin innholdsverdi) større enn mest
            mest = tall #sett mest er lik key sin innholdsverdi
            navn = i #sett navn er lik key
    print("\nMaanedens ansatte er " + navn + " med " + str(mest) + " salg.")






ordbok2 = innlesning("salgstall.txt")
maanedensSalgsperson(ordbok2)










def totaltAntallSalg(ordbokTo):
    summen = 0 #sett summen til verdi 0
    for i in ordbokTo:
        salg = int(ordbokTo[i]) #for hver key i ordbok, key sin innholdsverdi blir et heltall og settes inni variabel salg
        if salg > 0: #hvis salg større enn 0
            summen+=salg #summen blir da summen pluss salg
    return summen










def gjennomsnittSalg(ordbokTre):
    summen = 0
    for i in ordbokTre:
        salg = int(ordbokTre[i])
        if salg > 0:
            summen+=salg
    gjennomsnitt = summen / len(ordbokTre)  #gjennomsnitt blir summen deler på lengde av ordboka som er antall selgere
    return gjennomsnitt









def hovedprogram():
    antallSelgere = str(len(ordbok2))
    total = str(totaltAntallSalg(ordbok2))
    perPerson = str(gjennomsnittSalg(ordbok2)) #konverter alle int til streng

    print("\nAktive selgere denne maaneden: " + antallSelgere)
    print("Totalt antall salg: " + total)
    print("Gjennomsnittlig antall salg per salgsperson: " + perPerson)



hovedprogram()
