import time
import random

stage = 0

def stages(stage):
    if stage == 0:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("=========")
    if stage == 1:
        print(" ")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if stage == 2:
        print("  +")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if stage == 3:
        print("  +---")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if stage == 4:
        print("  +---+")
        print("  |   |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
    if stage == 5:
        print("  +---+")
        print("  |   |")
        print("  |   O")
        print("  |  /|\ ")
        print("  |")
        print("  |")
        print("=========")
    if stage == 6:
        print("  +---+")
        print("  |   |")
        print("  |   O")
        print("  |  /|\ ")
        print("  |  / \ ")
        print("  |")
        print("=========")

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

for i in range(9):
    print(" ")

print("TIP: Om het hele woord te raden type ?")
print(" ")
geheimewoord = input("voer het gehieme woord in : ")
gebruikteletters = []
for i in range(20):
    print(" ")
while True:
    stages(stage)
    if stage == 6:
        print("helaas, u bent af")
        break
    for i in gebruikteletters:
        print(i + ", ", end='')
    print(" ")
    letter = input("voer een letter in om het woord te raden : ")
    if letter == "qwertyuiop":
        break
    aantal = len(letter)
    if letter in "abcdefghijklmnopqrstuvwxyz" and aantal == 1:
        if letter not in geheimewoord:
            print("u heeft een foute letter gekozen, probeer het nog een keer!")
            stage += 1
            print(stage)
        elif letter in gebruikteletters:
            print("u heeft deze letter al gebruikt, gebruik een andere letter")

        elif letter in geheimewoord:
            print("letter zit in het woord!")
        gebruikteletters.append(letter)
    else:
        print("potverdikkie dat is geen letter probeer een ECHTE letter!")