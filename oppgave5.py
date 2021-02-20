# Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil (tommer.txt) der hver linje beskriver et navn på et mål og selve målet i tommer. La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål og¨benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene i centimeter.

minFil = open("tommer.txt") #åpne txt-fil

minList = []
minOrdbok = {}




def ordbok(): #opprett en funksjon ordbok
    for linje in minFil:
        biter = linje.split(" ") #hver linje i filen blir splittet etter mellomrom og blir til en liste som inneholder to verdier.
        minList.append(biter) #setter liste inni minList, slik at det blir tre lister inni en liste

    minOrdbok = dict(minList)  #konvertere minList til en ordbok
    return minOrdbok #returnere ordbok og avlustter funksjon




minOrdbok = ordbok() #setter funksjon inni en tom ordbok, siden funksjonen returnerer ordbok, så minOrdbok blir en ordbok som inneholder minList





def tommerTilCm(antallTommer): #definer funksjon tommerTilcm
    assert antallTommer > 0  #parameteren må ha verdi større enn 0 ellers stopper programmet og viser asserterror
    cm = antallTommer*2.54
    return cm






def tommerregning():#opprett prosedyre
    verdiEn = float(minOrdbok["Skulderbredde"]) #konverterer hver nøkkelverdi sin innholdsverdi til et flytttal, og setter inni variablen
    verdiTo = float(minOrdbok["Halsvidde"])
    verdiTre = float(minOrdbok["Livvidde"])

    maalEn = str(tommerTilCm(verdiEn))  #kall funksjon tommerTilCm med parametere, og konvertere til string, deretter setter verdi inni variablen
    maalTo = str(tommerTilCm(verdiTo))
    maalTre = str(tommerTilCm(verdiTre))

    print("Skulderbredde er " + str(verdiEn) + " tommer som tilsvarer " + maalEn + " centimeter.") #printer ut resultat
    print("Halsvidde er " + str(verdiTo) + " tommer som tilsvarer " + maalTo + " centimeter.")
    print("Livvidde er " + str(verdiTre) + " tommer som tilsvarer " + maalTre + " centimeter.")



tommerregning() #kall prosedyren
