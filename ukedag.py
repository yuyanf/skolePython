class Ukedag:
  def __init__(self, dag):
    self._dag = dag
    aktivitetListe = []

  def settInn(self, hva, kl):
    nyAktivitet = Aktivitet(hva, kl)
    if not aktivitetListe:
      aktivitetListe.append(nyAktivitet)
    else:
      for i in aktivitetListe:
        if i.hentKl() != kl:
          aktivitetListe.append(nyAktivitet)
        else:
            print("Denne time er opptatt.")


  def tidligste(self):
    if not aktivitetListe:
      return -1
    else:
      tidlig = aktivitetListe[0].hentKl()
      for i in aktivitetListe:
        if i.hentKl() < tidlig:
          tidlig = i.hentKl()
      return tidlig


  def seneste(self):
    sen = 0
    if not aktivitetListe:
    return -1
    else:
      for i in aktivitetListe:
        if i.hentKl() > sen:
          sen = i.hentKl()
      return sen


  def antall(self):
    antall = len(aktivitetListe)
    return antall



    def settInnLedig(self, hva):
        if self.antall() == 24:
            print("dagens aktivitet er fult")

        elif not aktivitetListe:
            endaAktivitet = Aktivitet(hva, 12)
            aktivitetListe.append(endaAktivitet)

        else:
            antall = self.antall()
            for klokke in range(self.tidliste()+1, self.seneste()):
                for i in aktivitetListe:
                    if i.hentKl() != klokke:
                        self.settInn(hva, klokke)
            if antall == len(aktivitetListe) and self.seneste() < 23:
                endaAktivitet = Aktivitet(hva, self.seneste()+1)
                aktivitetListe.append(endaAktivitet)

            elif antall == len(aktivitetListe):
                endaAktivitet = Aktivitet(hva, self.tidligste()-1)
                aktivitetListe.append(endaAktivitet)
