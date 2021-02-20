#Programmet tar i mot alder og vekt til en hund og sett metthet til 10. Vekten skal endre seg ut ifra hvordan mettheten endrer seg.

class Hund:

    def __init__(self,alder,vekt,metthet):
        self.alder = alder
        self.vekt = vekt
        self.metthet = metthet #instansvariabler alder, vekt og metthet


    def printUt(self):
        print("\nAlder til din hund er", str(self.alder)+" måneder.", "\nVekt til din hund nå er", str(self.vekt)+" kg.")
        print()



    def spring(self):
        self.metthet = self.metthet - 1 #metthet er nå 9
        if self.metthet < 5:  #hvis metthet er mindre enn 5
            self.vekt = self.vekt - 1  #vekt minus 1



    def spis(self,tall):
        self.metthet = self.metthet + int(tall)  #legg et heltall inni metthet
        if self.metthet > 7: #hvis metthett større enn 7
            self.vekt = self.vekt + 1 #vekt pluss 1
