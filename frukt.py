class Frukt:
    def __init__(self, navn, vann, spiselig):
        self._navn = navn
        self._vann = vann
        self._spiselig = spiselig

    def hentVannPr100(self):
        return self._vann

    def erSpiselig(self):
        if self._spiselig != "ukjent":
            return True


    def __str__(self):
        s = self._navn + "\n" + str(self._vann) + "\n" + self._spiselig
        return s
