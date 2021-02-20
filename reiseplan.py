#Programmet lager tre lister først, deretter ber brukere taster inn to tilfeldige tall, og bruker if-sjekk til å skrive ut lista/elementen som tilsværer tallene brukere taster inn.
steder = []
klesplagg = []
avreisedatoer = []

x = range(5) # range 5 er fra posisjon 0 til 4 i x
for i in x: # for hver i in x
    reisemål = input("Skriv et reisemål: ")
    steder.append(reisemål)  #legger hver element inni lista
    klær = input("Skriv et klesplagg: ")
    klesplagg.append(klær)
    dato = input("Skriv en dato: ")
    avreisedatoer.append(dato)


reiseplan = [steder , klesplagg , avreisedatoer]


for i in reiseplan:
    print(i)


i1 = int(input("Tast inn tall1: "))
i2 = int(input("Tast inn tall2: ")) #gjør input til heltall

if i1 >= 0 and i1 <= 2 and i2 >= 0 and i2 <= 4:  #hvis i1 er mellom 0 og 2 og i2 er mellom 0 og 4
    print("Tall1 du tastet inn tilsværer denne lista:")
    print(reiseplan[i1]) #reiseplan er en liste av liste, liste med posisjon i1 blir skrevet ut
    print("Tall2 du tastet inn tilsværer denne elementen fra lista:")
    indeks = reiseplan[i1] #deklarere indeks er den lista
    print(indeks[i2]) #element med posisjon i2 i den lista blir skrevet ut
else:
    print("Ugyldig input!")
