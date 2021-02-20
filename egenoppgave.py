#Oppgaveteskt: Lag et quiz med spørsmål "Apollo 11 var navnet på ekspedisjonen til månen, men landingsfartøyet, som tok Neil Armstrong og Buzz Aldrin ned på månens overflate, hadde et eget navn. Hva var det?" og gir tilbakemelding på om svarene er korrekte. Quiz skal gjentas til brukere klarte å svare riktig.
def quiz(): #definere kode quiz
    svar=input()
    svar=svar.lower() #uansett hva brukere skriver inn regnes som små bokstaver
    if svar == "eagle":
        print("Riktig din smarting!")
    else:
        print("Feil svar. Nå får du tre alternativ: \nA: Eagle B: Enterprise C: USS George Washinton  Prøv igjen!")
        quiz() #dersom svar er feil, linje 8 er skrevet ut til terminalen, og i tillegg vil kode quiz kjøres igjen fra linje 3. Dersom svar er feil igjen, gjentar det seg til brukere svarer riktig, slik har jeg laget en loop.
svar = input("Quiz time!\nApollo 11 var navnet på ekspedisjonen til månen, men landingsfartøyet, som tok Neil Armstrong og Buzz Aldrin ned på månens overflate, hadde et eget navn. Hva var det?\n")
svar=svar.lower()
if svar == "eagle": #if-sjekk er nødvendig å ha her. Dersom jeg kaller quiz først, vil kode starte fra linje 3, dvs. programmet vil ikke gi respons første gang etter brukere har svart.
    print("Riktig din smarting!")
else:
    print("Feil svar. Nå får du tre alternativ: \nA: Eagle B: Enterprise C: USS George Washinton  Prøv igjen!")
    quiz() #kaller quiz
