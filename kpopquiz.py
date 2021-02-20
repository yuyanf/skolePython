#Lag en kpop quiz, med 3 spørsmål. Spørsmålet og svaret skal være i en ordbok.
#Print deretter ut spørsmålene og be bruker skrive inn svar. Samle opp poengene og skriv ut
#poengsummen tilslutt.

print("Quiz time! Du skal svare tre spørsmål i tema-KPOP. Svar med A, B eller C")
spørsmål1 = "1. Hvilket år er BTS debut i?\nA:2013  B:2011  C:2014"
spørsmål2 = "2. Hvor mange fins i gruppen-SEVENTEEN?\nA:12  B:11  C:13"
spørsmål3 = "3. Tilhører gruppen-Red Velvet SM Entertaiment?\nA:Ja  B:Nei  C:Vet ikke"


kpop = {
    spørsmål1 : "A",
    spørsmål2 : "C",
    spørsmål3 : "A",
}

poeng = 0

for x in kpop:
    print(x)
    svar = input()
    svar=svar.upper()
    if svar == kpop[x]:
        poeng += 1

print("Poengsum:", poeng)
