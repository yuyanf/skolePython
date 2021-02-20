#Lag et program der du legger inn 5 navn og bursdager i lister. Deretter skal 5 navn skrevet ut til terminalen og ber brukere taste inn ett navn og får tilhørende bursdag skrevet ut til terminalen. Brukere kan avslutte programmet når de vil, ellers kjører programmet i loop slik at brukere får sjekka alle 5 bursdager.

list1 = ["Anton Vo", "09.03.1994"]
list2 = ["Jenny Fei", "02.11.1994"]
list3 = ["Ludo Fei", "27.02.2019"]
list4 = ["Luna Chien", "25.10.2018"]
list5 = ["Mireille Marie", "10.08.1994"]

listAlle = [list1[0], list2[0], list3[0], list4[0], list5[0]]
listAlle2 = [list1, list2, list3, list4, list5]



print("Hei! Du har fått 5 nye venner:D")
print(listAlle)
print("Tast inn navnet for å sjekke vennens bursdag. Tast inn Avslutt for exit når som helst")


x = range(100)
for i in x:
    navn = input("Navn: (eller Avslutt) ")
    if navn == "Avslutt":
        break

    elif navn in listAlle:
        x = listAlle.index(navn)
        resultat = listAlle2[x]
        print(resultat)

    else:
        print("Ugyldig navn!")
