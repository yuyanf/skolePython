class Student:
  def __init__(self, navn, brukernavn, tel):
    self._navn = navn
    self._brukernavn = brukernavn
    self._tel = tel

  def __str__(self):
    s = "Navn: " + self._navn + "\nBrukernavn: " + self._brukernavn + "\nTelefonnr: " + str(self._tel)
    return s
