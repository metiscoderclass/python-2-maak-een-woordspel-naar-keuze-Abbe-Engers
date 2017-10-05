import time


def voortgang():
    galg()
    print()
    for i in geradenwoord:
        print(i + " ", end='')
    print("")
    print("")
    for i in geradenletters:
        print(i + ", ", end='')
    print("")
    print("")

def galg():
    for i in range(40):
            print("")
    if foutgeraden == 0:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("=========")
    if foutgeraden == 1:
        print(" ")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if foutgeraden == 2:
        print("  +")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if foutgeraden == 3:
        print("  +---")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if foutgeraden == 4:
        print("  +---+")
        print("  |   |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if foutgeraden == 5:
        print("  +---+")
        print("  |   |")
        print("  |   O")
        print("  |  /|\ ")
        print("  |")
        print("  |")
        print("=========")
    if foutgeraden == 6:
        print("  +---+")
        print("  |   |")
        print("  |   O")
        print("  |  /|\ ")
        print("  |  / \ ")
        print("  |")
        print("=========")



for i in range(9):
    print(" ")

print("888")
print("888")
print("888")
print("88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.")
print("888 _88b    _88b888 _88bd88P_88b888 _888 _88b    _88b888 _88b")
print("888  888.d888888888  888888  888888  888  888.d888888888  888")
print("888  888888  888888  888Y88b 888888  888  888888  888888  888")
print("888  888_Y888888888  888 _Y88888888  888  888_Y888888888  888")
print("                             888")
print("                         Y8b d88")
print("                          _Y88P")

for i in range(20):
    print("")

print("TIP: Om het hele woord te raden type ?")
print(" ")
geheimewoord = input("voer het gehieme woord in : ")
gebruikteletters = [""]

while True:
    letter = input("voer een letter in om het woord te raden : ")
    if letter == "stop":
        break
    aantal = len(letter)
    if letter in "abcdefghijklmnopqrstuvwxyz" and aantal == 1:
        if letter not in geheimewoord:
            print("u heeft een foute letter gekozen!")

        elif letter in gebruikteletters:
            print("u heeft deze letter al gebruikt")

        elif letter in geheimewoord:
            print("letter zit in het woord!")
        gebruikteletters.append(letter)
    else:
        print("potverdikkie dat is geen goede letter!")
