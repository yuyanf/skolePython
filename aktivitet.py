class Aktivitet:
  def __init__(self, hva, kl):
    self._aktNavn = hva
    self._start = kl


    def hentKl(self):
        return self._start 
