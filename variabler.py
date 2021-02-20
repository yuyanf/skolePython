#Programmet spør hva studenten heter og hilser på studenten
print("Hei Student!") #"print" funksjon skriver ut tekst til terminal, og tekst må ha ""
navn = input("Vennligst skriv navnet ditt her:\n") #"input" funksjon henter verdi fra det brukeren skriver inn, og variabel"navn" tilsettes verdien. "\n" er for linjeskift
print("Hei", navn) #variabel trenger ikke ""

#programmet finner ut differansen mellom 2 tall
tall1 = 3 #variabel "tall1" har en heltallsverdi som er 3
print(tall1) #print skriver ut verdi 3 til terminal
tall2 = 7
print(tall2)
differanse = tall1 - tall2 #nå gir jeg den tredje variablen "differanse" en verdi som er variabel 1 minus variabel 2
print("Differanse:", differanse) #her ber jeg "print" skriver ut verdien fra den tredje variablen

#programmet ber brukere å skrive et nytt navn og slår sammen begge navn
navn2 = input("Vennligst skriv et nytt navn her:\n") #variabel "navn2" tilsettes verdien fra "input" funksjon som er et nytt navn brukeren skrier inn
sammen = navn + navn2 #variabel "sammen" er gitt verdi som er det første navn pluss det andre navn
print(sammen)

sammen = navn + " og " + navn2 #jeg endrer sammen ved å legge til test " og " mellom navn og navn2
print(sammen) #print skriver ut den nye versjon av variabel sammen til terminal
