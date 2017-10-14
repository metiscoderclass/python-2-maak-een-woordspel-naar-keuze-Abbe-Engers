import time
import random

lijstwoorden = ["aan", "aanbod", "aanraken", "aanval", "aap", "aardappel", "aarde", "aardig", "acht", "achter", "actief", "activiteit", "ademen", "af", "afgelopen", "afhangen", "afmaken", "afname", "afspraak", "afval", "al", "algemeen", "alleen", "alles", "als", "alsjeblieft", "altijd", "ander", "andere", "anders", "angst", "antwoord", "antwoorden", "appel", "arm", "auto", "avond", "avondeten", "baan", "baby", "bad", "bal", "bang", "bank", "basis", "bed", "bedekken", "bedreiging", "bedreven", "been", "beer", "beest", "beetje", "begin", "begrijpen", "begrip", "behalve", "beide", "beker", "bel", "belangrijk", "bellen", "belofte", "beneden", "benzine", "berg", "beroemd", "beroep", "bescherm", "beslissen", "best", "betalen", "beter", "bevatten", "bewegen", "bewolkt", "bezoek", "bibliotheek", "bieden", "bij", "bijna", "bijten", "bijvoorbeeld", "bijzonder", "binnen", "binnenkort", "blad", "blauw", "blazen", "blij", "blijven", "bloed", "bloem", "bodem", "boek", "boerderij", "boete", "boom", "boon", "boord", "boos", "bord", "borstelen", "bos", "bot", "bouwen", "boven", "branden", "brandstof", "breed", "breken", "brengen", "brief", "broer", "broek", "brood", "brug", "bruikbaar", "bruiloft", "bruin", "bui", "buiten", "bureau", "buren", "bus", "buurman", "buurvrouw", "cadeau", "chocolade", "cirkel", "comfortabel", "compleet", "computer", "conditie", "controle", "cool", "correct", "daar", "daarom", "dag", "dak", "dan", "dansen", "dapper", "dat", "de", "deel", "deken", "deksel", "delen", "derde", "deze", "dichtbij", "dienen", "diep", "dier", "dik", "ding", "dit", "dochter", "doen", "dom", "donker", "dood", "door", "doorzichtig", "doos", "dorp", "draad", "draaien", "dragen", "drie", "drijven", "drinken", "drogen", "dromen", "droog", "druk", "dubbel", "dun", "dus", "duur", "duwen", "echt", "een", "één", "eend", "eenheid", "eenzaam", "eerste", "eeuw", "effect", "ei", "eigen", "eiland", "einde", "eis", "elektrisch", "elk", "en", "enkele", "enthousiast", "erg", "eten", "even", "examen", "extreem", "falen", "familie", "feest", "feit", "fel", "fijn", "film", "fit", "fles", "foto", "fout", "fris", "fruit", "gaan", "gat", "gebeuren", "gebeurtenis", "gebied", "geboorte", "geboren", "gebruik", "gebruikelijk", "gebruiken", "gedrag", "gedragen", "geel", "geen", "gehoorzamen", "geit", "geld", "geliefde", "gelijk", "geloof", "geluid", "geluk", "gemak", "gemakkelijk", "gemeen", "genieten", "genoeg", "genot", "gerecht", "gereedschap", "geschikt", "gespannen", "geur", "gevaar", "gevaarlijk", "gevangenis", "geven", "gevolg", "gewicht", "gewoon", "gezicht", "gezond", "gif", "gisteren", "glad", "glas", "glimlach", "god", "goed", "goedkoop", "goud", "graf", "grap", "grappig", "gras", "grens", "grijs", "groeien", "groen", "groente", "groep", "grof", "grond", "groot", "grootmoeder", "grootvader", "haan", "haar", "haast", "hal", "halen", "half", "hallo", "hamer", "hand", "hard", "hart", "haten", "hebben", "heel", "heet", "helder", "helft", "help", "hem", "hemel", "hen", "herfst", "herinneren", "hert", "het", "heuvel", "hier", "hij", "hobby", "hoe", "hoed", "hoek", "hoeveel", "hoeveelheid", "hoewel", "hond", "honderd", "honger", "hoofd", "hoog", "hoogte", "hoop", "horen", "hotel", "houden", "huilen", "huis", "hun", "huren", "hut", "huur", "idee", "ieder", "iedereen", "iemand", "iets", "ijs", "ijzer", "ik", "in", "instrument", "ja", "jaar", "jagen", "jas", "jij", "jong", "jongen", "jouw", "jullie", "kaars", "kaart", "kaas", "kamer", "kans", "kant", "kantoor", "kap", "kast", "kasteel", "kat", "kennen", "kennis", "keuken", "keus", "kiezen", "kijken", "kind", "kip", "kist", "klaar", "klas", "klasse", "kleden", "klein", "kleren", "kleur", "klimmen", "klok", "kloppen", "klopt", "knie", "knippen", "koers", "koffer", "koffie", "kok", "koken", "kom", "komen", "koning", "koningin", "koorts", "kop", "kopen", "kort", "kost", "kosten", "koud", "kraam", "kracht", "krant", "krijgen", "kruis", "kuil", "kunnen", "kunst", "laag", "laat", "laatst", "lach", "lachen", "ladder", "laken", "lamp", "land", "lang", "langs", "langzaam", "laten", "leeftijd", "leeg", "leerling", "leeuw", "leger", "leiden", "lenen", "lengte", "lepel", "leren", "les", "leuk", "leven", "lezen", "lichaam", "licht", "liefde", "liegen", "liggen", "lijk", "lijken", "liniaal", "links", "lip", "list", "lomp", "lood", "lopen", "los", "lot", "lucht", "lui", "luisteren", "lunch", "maag", "maal", "maaltijd", "maan", "maand", "maar", "maat", "machine", "maken", "makkelijk", "mama", "man", "mand", "manier", "map", "markeren", "markt", "me", "medicijn", "meel", "meer", "meerdere", "meest", "meisje", "melk", "meneer", "mengsel", "mensen", "mes", "met", "meubel", "mevrouw", "middel", "midden", "mij", "mijn", "miljoen", "min", "minder", "minuut", "mis", "missen", "mits", "model", "modern", "moeder", "moeilijk", "moeten", "mogelijk", "mogen", "moment", "mond", "mooi", "moord", "moorden", "morgen", "munt", "muziek", "na", "naald", "naam", "naar", "naast", "nacht", "nat", "natuur", "natuurlijk", "nee", "neer", "negen", "nek", "nemen", "net", "netjes", "neus", "niet", "niets", "nieuw", "nieuws", "nobel", "noch", "nodig", "noemen", "nog", "nood", "nooit", "noord", "noot", "normaal", "nu", "nul", "nummer", "object", "oceaan", "ochtend", "oefening", "of", "offer", "olie", "olifant", "om", "oma", "onder", "onderwerp", "onderzoek", "oneven", "ongeluk", "ons", "ontsnappen", "ontbijt", "ontdekken", "ontmoeten", "ontvangen", "ontwikkelen", "onze", "oog", "ooit", "ook", "oom", "oor", "oorlog", "oorzaak", "oost", "op", "opa", "opeens", "open", "openlijk", "opleiding", "opnemen", "oranje", "orde", "oud", "ouder", "over", "overal", "overeenkomen", "overleden", "overvallen", "paar", "paard", "pad", "pagina", "pan", "papa", "papier", "park", "partner", "pas", "passeren", "pen", "peper", "per", "perfect", "periode", "persoon", "piano", "pijn", "pistool", "plaat", "plaatje", "plaats", "plafond", "plank", "plant", "plastic", "plat", "plattegrond", "plein", "plus", "poes", "politie", "poort", "populair", "positie", "postzegel", "potlood", "praten", "presenteren", "prijs", "prins", "prinses", "privé", "proberen", "probleem", "product", "provincie", "publiek", "punt", "raak", "raam", "radio", "raken", "rapport", "recht", "rechtdoor", "rechts", "rechtvaardig", "redden", "reeds", "regen", "reiken", "reizen", "rekenmachine", "rennen", "repareren", "rest", "restaurant", "resultaat", "richting", "rijk", "rijst", "rijzen", "ring", "rok", "rond", "rood", "rook", "rots", "roze", "rubber", "ruiken", "ruimte", "samen", "sap", "schaap", "schaar", "schaduw", "scheiden", "scherp", "schetsen", "schieten", "schijnen", "schip", "school", "schoon", "schouder", "schreeuw", "schreeuwen", "schrijven", "schudden", "seconde", "sex", "signaal", "simpel", "sinds", "slaapkamer", "slapen", "slecht", "sleutel", "slim", "slot", "sluiten", "smaak", "smal", "sneeuw", "snel", "snelheid", "snijden", "soep", "sok", "soms", "soort", "sorry", "speciaal", "spel", "spelen", "sport", "spreken", "springen", "staal", "stad", "stap", "start", "station", "steen", "stelen", "stem", "stempel", "ster", "sterk", "steun", "stil", "stilte", "stoel", "stof", "stoffig", "stom", "stop", "storm", "straat", "straffen", "structuur", "student", "studie", "stuk", "succes", "suiker", "taal", "taart", "tafel", "tak", "tamelijk", "tand", "tante", "tas", "taxi", "te", "team", "teen", "tegen", "teken", "tekenen", "telefoon", "televisie", "tellen", "tennis", "terug", "terugkomst", "terwijl", "test", "tevreden", "thee", "thuis", "tien", "tijd", "titel", "toekomst", "toen", "toename", "totaal", "traan", "tram", "trein", "trekken", "trouwen", "trui", "tuin", "tussen", "tweede", "u", "uit", "uitleggen", "uitnodigen", "uitvinden", "uitzoeken", "uur", "vaak", "vaarwel", "vader", "vak", "vakantie", "vallen", "vals", "van", "vandaag", "vangen", "vanmorgen", "vannacht", "varken", "vast", "vechten", "veel", "veer", "veilig", "ver", "veranderen", "verandering", "verder", "verdienen", "verdrietig", "verenigen", "verf", "vergelijkbaar", "vergelijken", "vergelijking", "vergeten", "vergeven", "vergissen", "verhaal", "verhoging", "verjaardag", "verkeerd", "verkopen", "verlaten", "verleden", "verliezen", "vernietigen", "veroveren", "verrassen", "vers", "verschil", "verschrikkelijk", "verspreiden", "verstand", "verstoppen", "versturen", "vertellen", "vertrekken", "vertrouwen", "verwachten", "verwijderen", "verzamelen", "verzameling", "vet", "vier", "vierkant", "vies", "vijand", "vijf", "vijver", "vinden", "vinger", "vis", "vlag", "vlees", "vlieg", "vliegtuig", "vloer", "voeden", "voedsel", "voelen", "voet", "voetbal", "vogel", "vol", "volgende", "volgorde", "voor", "voorbeeld", "voorkomen", "voorzichtig", "voorzien", "vork", "vorm", "vos", "vouwen", "vraag", "vragen", "vrede", "vreemd", "vreemde", "vriend", "vriendelijk", "vriezen", "vrij", "vrijheid", "vroeg", "vroeger", "vrouw", "vullen", "vuur", "waar", "waarom", "waarschijnlijk", "wachten", "wakker", "wanneer", "want", "wapen", "warm", "wassen", "wat", "water", "we", "week", "weer", "weg", "welke", "welkom", "wens", "wereld", "werelddeel", "werk", "west", "wetenschap", "wie", "wiel", "wij", "wijn", "wijs", "wild", "willen", "wind", "winkel", "winnen", "winter", "wissen", "wit", "wolf", "wolk", "wonder", "woord", "woud", "wreed", "zaak", "zacht", "zak", "zand", "zee", "zeep", "zeer", "zeggen", "zeil", "zeker", "zelfde", "zes", "zetten", "zeven", "ziek", "ziekenhuis", "ziel", "zien", "zij", "zijn", "zilver", "zingen", "zinken", "zitten", "zo", "zoals", "zoeken", "zoet", "zomer", "zon", "zonder", "zonnig", "zoon", "zorg", "zorgen", "zou", "zout", "zuid", "zulke", "zullen", "zus", "zwaar", "zwak", "zwembad", "zwemmen", "grafeem", "tjiftjaf", "maquette", "kitsch", "pochet", "convocaat", "jakkeren", "collaps", "zuivel", "cesium", "voyant", "spitten", "pancake", "gietlepel", "karwats", "dehydreren", "viswijf", "flater", "cretonne", "sennhut", "tichel", "wijten", "cadeau", "trotyl", "chopper", "pielen", "vigeren", "vrijuit", "dimorf", "kolchoz", "janhen", "plexus", "borium", "ontweien", "quiche", "ijverig", "mecenaat", "falset", "telexen", "hieruit", "femelaar", "cohesie", "exogeen", "plebejer", "opbouw", "zodiak", "volder", "vrezen", "convex", "verzenden"]
geheimewoord = random.choice(lijstwoorden)

aantalgeraden = 0

def checkgoed():
    for b in range(len(geheimewoord)):
        if not geheimewoord[b] in goedgeradenletters:
            return(False)
    return(True)

stage = 0

goedgeradenletters = []

foutgeradenletters = []

letterswoord = []

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

for i in range(10):
    print("")

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
    print(" ")

print("TIP: Om het hele woord te raden type ?")

time.sleep(2)

gebruikteletters = []
for i in range(20):
    print(" ")
while True:
    for i in range(17):
        print(" ")
    stages(stage)
    for i in range(3):
        print("")
    if stage == 6:
        print("helaas, u bent af")
        print(" ")
        print("het woord was " + geheimewoord)
        break
    for i in foutgeradenletters:
        print(i + ", ", end='')
    print(" ")
    letter = input("voer een letter in om het woord te raden : ")
    if letter == "qq":
        break
    if letter == "?":
        woordraden = input("voer een woord in om te raden : ")
        if woordraden == geheimewoord:
            print("je hebt het woord goed geraden")
            break
        else:
            print("helaas")
            stage+=1
    aantal = len(letter)
    if letter in "abcdefghijklmnopqrstuvwxyz" and aantal == 1:
        if letter not in geheimewoord:
            print("u heeft een foute letter gekozen, probeer het nog een keer!")
            stage += 1
            foutgeradenletters.append(letter)

        elif letter in gebruikteletters:
            print("u heeft deze letter al gebruikt, gebruik een andere letter")

        elif letter in geheimewoord:
            print("letter zit in het woord!")
            goedgeradenletters.append(letter)
        gebruikteletters.append(letter)

    else:
        print("potverdikkie dat is geen letter probeer een ECHTE letter!")

    for i in range(30):
        print("")

    for a in geheimewoord:
        if a in goedgeradenletters:
            print(a, end=' ')
        else:
            print("_", end=' ')

    if aantalgeraden == len(geheimewoord):
        print("goedgeraden!!!")
        break

    if checkgoed():
        print(" is het goede woord")
        for i in range(5):
            print(" ")
        break