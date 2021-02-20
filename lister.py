#Programmet sjekker om brukere husker seg og lager lister.
liste1 = [3, 7, 9]
liste1.append(17)
print(liste1[0])
print(liste1[2])

liste2=[]
x = range(4) # range-funksjon sier at x skal ha 4 plasser
for ting in x: #så lenge det fins en verdi i første plass i x så skal undernevnt skje, også gjentar det seg til det ikke fins noe verdi i x lenger og da kan ikke undernevnt skje og da er for-funksjon ferdig.
    svar = input("oppgi et navn: ")
    liste2.append(svar)
print(liste2)

if "Jenny" in liste2:
    print("Du husker meg!")
else:
    print("Glemte du meg?")

summen=sum(liste1)
x = 1
for tall in liste1:
    x = x * tall
produkt=x
liste3=[summen, produkt]

liste4=[]
liste4=liste1+liste3
print(liste3)
print(liste4)


liste4.pop()
liste4.pop()
print(liste4)
