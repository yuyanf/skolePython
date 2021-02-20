#Programmet ber brukere å skrive en setning og teller hvor manger hver enkelt ord er skrevet og hvor mange bokstaver av hver enkelte ord.
def telling(ord):
    antall = len(ord)
    return antall



def telling2(setning):
    ordbok = {}  #deklarere ei tom ordbok
    ord = setning.split() #nå er setning splittet på hver mellomrom og blir en list-"ord"

    for i in ord:
        if i in ordbok: #hvis "i" in "ord" fins i "ordbok"
            ordbok[i]+=1 #"i" sin innholdsverdi pluss på 1
        else:
            ordbok[i] = 1#ellers sett "i" sin innholdsverdi til 1

    return ordbok



tekst = input("Skriv en setning:\n")
ordbok = telling2(tekst) #sett setningen i ordbok ved bruk av funksjon-telling2
antallord = telling(tekst.split()) #split setninger til enkle ord på hver mellomrom i en liste, og finner ut lengde av lista


print("Det er " + str(antallord) + " ord i setningen din.")

for i in ordbok:
    tall = str(ordbok[i]) #nøkkelverdi sin innholdsverdi er hvor mange ganger ordet forekommer
    lengde = str(telling(i)) #antall bokstaver av hvert ord ved bruk av funksjon-telling
    print("Ordet '" + i + "' forekommer " + tall + " ganger, og har " + lengde + " bokstaver")
