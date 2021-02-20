

liste = ["Lady Gaga", "Eplemann"]

if "Lady" in liste:
    print("Fant!")

def sjekk(navn):
    list = navn.split()
    print("Listen: ", list)
    print("Liste: ", liste)

    for j in list:
        print("i: ", j)
        for i in range(2):
            if j in liste[i]:
                print("funker")


sjekk("Lord Gaga")
