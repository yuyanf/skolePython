

class Julekalender:
    def __init__(self, alleBarna, navnFil):
        self._kalender = [] #24 Gave objeketer i kalendern.
        self._apnere = [] #fylt med barn
        self._nesteApnere = 0
        self._dag = 0
        self._lesGavefil(navnFil)


        for i in alleBarna:
            nyttBarn = Barn(i)
            self._apnere.append(nyttBarn)




    def nyDag(self):
        self._apnere[self._nesteApnere].apneGave(self._kalender[self._dag])

        if self._nesteApnere == len(self._apnere)-1:
            self._nesteApnere = 0
        else:
            self._nesteApenere += 1
        self._dag += 1


    def gaveOversikt(self):



    def _lesGavefil(self, fil):

        f = open(fil)
        for i in f:
            linja = i.split(",")
            nyGave = Gave(linja[0], int(linja[1]))
            self._kalender.append(nyGave)

        f.close()



jk = Julekalender([],"gave.txt") # dag 0 barn 0
jk.nyDag()1
jk.nyDag()2
jk.nyDag()3
