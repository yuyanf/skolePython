#Programmet importerer klasse Motorsykkel fra motorsykkel.py og lager tre objekter av klasse som skal skrives ut til terminalen. Siste objekt sin kilometerstand skal også oppdateres og skrive ut til terminalen.


from motorsykkel import Motorsykkel #import klasse fra motorsykkel.py


def hovedprogram():

    produktEn = Motorsykkel("Harley","XV45466", 5000)
    produktTo = Motorsykkel("BMW","JA97586", 300)
    produktTre = Motorsykkel("Suzuki","GK83348", 1000) #oppretter tre objekter av Motorsykkel

    produktEn.skrivUt()
    produktTo.skrivUt()
    produktTre.skrivUt() #skriv ut objektene

    produktTre.kjor(10) #oppdater kilometer
    print("\nNy kilometerstand til den tredje motorsykkelen er nå:", produktTre.hentKilometerstand(), "km.")



hovedprogram()
