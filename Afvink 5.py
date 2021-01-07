# Opdracht 1 Pet Class:
class pet:
    def __init__(self):
        """Geeft waardes aan leeftijd, naam en soort
        """
        self.__leeftijd = 0
        self.__naam = ""
        self.__soort = ""

    def setNaam(self, naam):
        """Set de naam van het object
        """
        self.__naam = naam

    def getNaam(self):
        """Return de naam van het object
        """
        return self.__naam

    def setLeeftijd(self, leeftijd):
        """Set de leeftijd van het object
        """
        self.__leeftijd = leeftijd

    def getLeeftijd(self):
        """Return de leeftijd van het object
        """
        return self.__leeftijd

    def setSoort(self, soort):
        """Set de soort van het object
        """
        self.__soort = soort

    def getSoort(self):
        """Return de soort van het object
        """
        return self.__soort


# Opdracht 2 Car Class:
class car:
    def __init__(self, model, speed):
        """Geeft waardes aan __year_model en __speed
        Vernelt bij het begin 5x, print de snelheid en dan 5x remmen waarbij na elke keer remmen
        de snelheid word geprint.
        """
        self.__year_model = model
        self.__speed = speed

        for i in range(5):
            self.__speed += 5
        print(self.__speed)

        for i in range(5):
            self.brake()
            print(self.__speed)

    def accelerate(self):
        """Voegt 5 toe aan de snelheid als deze functie word aangeroepen.
        """
        self.__speed += 5

    def brake(self):
        """Verminderd de snelheid met 5 als deze functie word aangeroepen.
        """
        self.__speed -= 5

    def get_speed(self):
        """Return de snelheid van het object.
        """
        return self.__speed


# Opdracht 9: Trivia Game:
class question:
    def __init__(self, vraag, antw1, antw2, antw3, antw4, juiste_antw):
        self.__vraag = vraag
        self.__antw1 = antw1
        self.__antw2 = antw2
        self.__antw3 = antw3
        self.__antw4 = antw4
        self.__juiste_antw = juiste_antw

    def set_vraag(self, vraag):
        self.__vraag = vraag

    def set_antw1(self, antw1):
        self.__antw1 = antw1

    def set_antw2(self, antw2):
        self.__antw2 = antw2

    def set_antw3(self, antw3):
        self.__antw3 = antw3

    def set_antw4(self, antw4):
        self.__antw4 = antw4

    def set_juiste_antw(self, juiste_antw):
        self.__juiste_antw = juiste_antw

    def get_vraag(self):
        return self.__vraag

    def get_antw1(self):
        return self.__antw1

    def get_antw2(self):
        return self.__antw2

    def get_antw3(self):
        return self.__antw3

    def get_antw4(self):
        return self.__antw4

    def get_juiste_antw(self):
        return self.__juiste_antw

    def stel_vraag(self):
        print("Vraag: " + self.__vraag + \
              "\n1. " + self.__antw1 + \
              "\n2. " + self.__antw2 + \
              "\n3. " + self.__antw3 + \
              "\n4. " + self.__antw4)


def start(vraag_objecten):
    print("\nTrivia Quiz")
    speler1_score = 0
    speler2_score = 0
    for i in range(10):
        if i % 2 == 0:
            print("\nSpeler 1 is aan de beurt:")
            vraag_objecten[i].stel_vraag()
            keuze = int(input("Vul het juiste antwoord in: "))
            if keuze == vraag_objecten[i].get_juiste_antw():
                speler1_score += 1
        else:
            print("\nSpeler 2 is aan de beurt:")
            vraag_objecten[i].stel_vraag()
            keuze = int(input("Vul het juiste antwoord in: "))
            if keuze == vraag_objecten[i].get_juiste_antw():
                speler2_score += 1

    print("\nScore speler 1: " + str(speler1_score))
    print("\nScore speler 2: " + str(speler2_score))
    if speler1_score > speler2_score:
        print("Speler 1 wint")
    elif speler2_score > speler1_score:
        print("Speler 2 wint")
    else:
        print("Gelijkspel")


def trivia():
    vragenlijst = []
    lijst = ["Dit is vraag 1", "Dit is vraag 2", "Dit is vraag 3",
             "Dit is vraag 4", "Dit is vraag 5",
             "Dit is vraag 6", "Dit is vraag 7", "Dit is vraag 8",
             "Dit is vraag 9", "Dit is vraag 10"]
    antwoorden_lijst = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
    for i in range(10):
        vr = lijst[i]
        antw1 = "Antwoord 1"
        antw2 = "Antwoord 2"
        antw3 = "Antwoord 3"
        antw4 = "Antwoord 4"
        vraag = question(vr, antw1, antw2, antw3, antw4, antwoorden_lijst[i])
        vragenlijst += [vraag]

    start(vragenlijst)
# Haal de # hieronder weg om de trivia te starten
# trivia()
