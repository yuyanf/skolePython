#Programmet ber brukere skrive to datoer på bestemt format og samenligner disse
print("Skriv inn dato 1, f.eks 1204 for 12.april:\n")
dato1 = input()
print("Nå skriv inn dato 2:\n")
dato2 = input()

if dato1[2:4] < dato2[2:4]:
    print("Riktig rekkefølge!")
elif dato1[2:4] > dato2[2:4]:
    print("Feil rekkefølge!")
elif dato1[2:4] == dato2[2:4] and dato1[0:2] < dato2[0:2]:
    print("Riktig rekkefølge!")
elif dato1[2:4] == dato2[2:4] and dato1[0:2] > dato2[0:2]:
    print("Feil rekkefølge!")
else:
    print("Samme dato!")
