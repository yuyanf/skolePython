#Programmet oppretter en klasse med konstruktør og tre metoder som skal brukes senere.

#Registrer merker, registreringsnummre og kilometerstand til motorsykkel. Oppdater kilometerstand ved behov
class Motorsykkel:

    #Konstruktør
    def __init__(self,merke,nummer,km): #i konstruktøren opprettes tre instansvariabler som tar imot tre argumenter
        self.merke = merke
        self.nummer = nummer
        self.km = km

    #øke kilometerstand ved å pluss på det gitte antall kilometer
    def kjor(self,km): #metoden tar imot en argument-km og oppdaterer verdi til variablen self.km fra konstruktøren
        self.km = self.km + km
    #viser resultat av nye kilometerstand
    def hentKilometerstand(self): #metoden returnerer verdi til variablen self.km
        return self.km
    #skriv ut merker, registreringsnummre og kilometerstand til motorsykkel
    def skrivUt(self):
        print("\nMerke: ", self.merke, "\nRegisteringsnummer: ", self.nummer, "\nKilometerstand: ", self.km)
