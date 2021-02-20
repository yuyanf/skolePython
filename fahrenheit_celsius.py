#Programmet ber brukere skriver en temperatur i fahrenheit og regner til celsius
print("Oppgi en temperatur i fahrenheit: ")
fahrenheit = int(input()) #her bruker jeg int() til å endre type til verdi variablen har.
print(str(fahrenheit)+"°F") #jeg vil ha med fahrenheit symbol, så jeg endrer fahrenheit fra tallsverdi til string
celsius = (int(fahrenheit)-32)*5/9 #for å regne ut celsius må jeg da endre fahrenheit til tallverdi igjen
output = round(celsius,2) #jeg runder temperatur i celsius til 2 desimaler ved å bruke round funksjon
print(str(output)+"°C")# til slutt endrer jeg output til string for å ha med celsius symbol
