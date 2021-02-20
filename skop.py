
print('''

Først definerer vi funksjon minFunkjson som ikke tar imot noen parametre. Deretter definerer vi funksjon hovedprogram som tar heller ikke imot noen parametre. Deretter kalles vi hovedprogram.
Inni hovedprogram opprettes en variabel a med verdi 42, og en variabel b med verdi 0, og skriver ut b til terminalen. Deretter settes vi a sin verdi inni b, altså b har nå verdi 42. Så kalles vi minFunksjon.
Inni minFunksjon oppretter vi en for-løkke med range 2, dvs. det looper to runder når x er 0 og x er 1.

Første runde når x er 0:
Opprettes en variabel c med verdi 2 og skriver ut c til terminalen. Deretter setter vi c er lik c pluss 1 som gir da en verdi 3. Deretter oppretter vi variabel b med verdi 10, og b er lik b pluss a. Deretter skriver ut b til terminalen.

Andre runde når x er 1:
Variabel c settes til verdi 2 og skriver ut til terminalen. Deretter setter vi c er lik c pluss 1 som gir en verdi 3. b settes til verdi 10, og b er lik b pluss a. Deretter skriver ut b til terminalen. For-løkka stopper å loope etter 2 runder, og vi avslutter funksjon minFunksjon og returnerer b sin verdi.

Men siden a er aldri definert, så b+=a blir error. Programmet stopper seg på første runde i for-løkka da det kommer til linje- b+=a. Så å kalle hovedprogram får man slike resultater:

0 (det er print(b) før error- a = minFunksjon())
2 (det er print(c) i første runde i for-løkka før error- b +=a i minFunksjon)
Error"

''')
