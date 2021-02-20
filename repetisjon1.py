#Programmet ber brukere skriver inn bokstaver og responderer ut ifra hva brukeren taster inn. Programmet avslutter ikke helt til brukere taster inn "s"

mineOrd = []

def slaaSammen(streng1, streng2): #definer slaaSammen
    sammen = streng1 + streng2
    return sammen



def skrivUt(liste): #definer skrivUt
    for i in liste:
        print(i)


tekst = 0
while tekst != "s":  #While-løkka looper så lenge tekst ikke er lik s. I første omgang er condition True fordi tekst var satt til verdi 0.
    tekst = input("Skriv inn en bokstav: ")  #ber input fra brukere
    if tekst == "i":    #hvis input er lik i
        svar1 = input("Skriv tekst en: ")
        svar2 = input("Skriv tekst to: ")
        resultat = slaaSammen(svar1,svar2) #setter parametre inni funksjon slaaSammen, og deretter kaller på funksjon i resultat
        mineOrd.append(resultat) #setter resultat sin verdi alltid bakerst i lista mineOrd
        print(mineOrd)

    elif tekst == "u":#hvis input er lik u
        skrivUt(mineOrd) #kaller funksjon skrivUt som printer ut hver element i lista
#etter linje 27 kjører programmet fra linje 17 igjen, og sjekker om input er lik s. Dersom input er hverken s, i eller u da ber programmet input fra brukere igjen og om igjen helt til input treffer en condition. 
