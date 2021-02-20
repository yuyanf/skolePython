#Programmet sammenligner to datoer og gir ut svar basert på rekkefølge.
print("Tast inn dato 1, først dag, så måned:")#først ber brukeren å taste inn en dato
dag1 = input("Dag: ")#variabel dag1 er opprettet
måned1 = input("Måned: ")#variabel måned1 er opprettet
print(dag1, måned1)#første dato skriver ut til terminal


print("Tast inn dato 2, først dag, så måned:")#deretter ber brukeren å taste inn en dato til
dag2 = input("Dag: ")#variabel dag2 er opprettet
måned2 = input("Måned: ")#variabel måned2 er opprettet
print(dag2, måned2)#andre dato skriver ut til terminal


if måned1 < måned2:#hvis måned1 er mindre enn måned2
    print("Riktig rekkefølge!")#da er det riktig rekkefølge
elif måned1 > måned2:#eller måned1 større enn måned2
    print("Feil rekkefølge!")#feil rekkefølge

elif måned1 == måned2 and dag1 < dag2:#eller lik måned men forskjellige dager som dag1 mindre enn dag2
    print("Riktig rekkefølge!")

elif måned1 == måned2 and dag1 > dag2:#eller lik måned men forskjellige dager som dag1 større enn dag2
    print("Feil rekkefølge!")

else :#eller lik måned og lik dag
    print("Samme dato!")
