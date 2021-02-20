#Programmet ber brukere å taste inn tall helt til brukere taster inn 0 og da slutter programmet. I tillegg til det skal programmet regne ut hva er summen til de tallene, og hva er største og minste tall.
minlist = []
tall = 1

while tall != 0:
    svar = input("Tast inn et tall: ")
    tall = float((svar))#tall starter med verdi 1 så conditon er true altså tall ikke er lik 0- while-løkke starter å loope- be brukere skriver inn et tall(må ikke være heltall) og setter denne verdien inni variablen tall. While-løkka stopper å loope når condition ikke er true lenger som er tall er lik 0.
    #if tall != 0:
    minlist.append(tall) #Dersom 0 skal ikke være med i lista, kommenterer jeg ut linje 8

print("\nListe: ")

for i in minlist:
    print(i)


minSum = 0
for i in minlist:
    minSum += i

print("\nSummen av tallene du tastet inn er: " + str(minSum))


maks = 0
for i in minlist:
    if maks < i:
        maks = i

print("Største tall i lista di er: " + str(maks))


minst = maks
for i in minlist:
    if i < minst:
        minst = i

print("Minste tall i lista di er: " + str(minst))
