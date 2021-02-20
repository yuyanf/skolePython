#Dette programmet stiller bruker et spørsmål og responderer med tekst.
svar = input("Skal du ha en brus? Vennligst svar ja/nei (liten bokstav)\n")#variabel svar tilsettes verdi fra input funksjonen som er "ja" eller "nei" brukere er bedt om å skrive inn
if svar == "ja": #hvis svar tilsværer tekst-verdi "ja" (viktig at det er små bokstaver på if, og det er dobbelt likhetstegn og : ved slutten)
    print("Her har du en brus!") #print skriver ut denne til terminal, print ligger under if-sjekk og må tab inn.
elif svar == "nei": #hvis svar tilsværer teskt-verdi "nei" (elif betyr else if... hvis if er ikke True, da går det videre til elif)
    print("Den er grei.") #print skriver ut denne til terminal
else: #hvis både if og elif er False, da går det videre til else. else er alltid ved slutten og betyr hvis ingen overnevnt stemmer, skal else utføres. Det kan bare ha en else i if-sjekk
    print("Det forstod jeg ikke helt.")
