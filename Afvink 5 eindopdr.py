#Afvink 5:
class DNA:
    """Geeft waarden aan seq, RNA, lengte en gcp
    """
    def __init__(self, seq):
        self.__seq = seq
        self.__RNA = ""
        self.__lengte = ""
        self.__gcp = ""

    """Telt het aantal ATCGN en kijkt of dit gelijk is aan de totale lengte. Als dat zo is,
    betekend het dat het DNA is.
    """
    def setDNA(self, seq):
        seq = seq.upper
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        n = seq.count("N")
        tot = a+t+c+g+n
        lengte = len(seq)
        if lengte == tot:
            print("Dit is DNA")
            self.__seq = seq
        else:
            print("DNA bestaat alleen uit ACTGN")

    def getDNA(self):
        """Return seq
        """
        return self.__seq

    def getTranscript(self):
        """Vertaald de sequentie naar RNA en returned dit
        """
        RNA = seq.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
        RNA = RNA.upper
        print("Het RNA is: ", RNA)
        self.__RNA = RNA
        return self.__RNA

    def getLength(self):
        """Berekent de lengte van de sequentie
        """
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        n = seq.count("N")
        tot = a + t + c + g + n
        lengte = len(seq)
        print("De lengte van de sequentie is ", lengte, "nucleotiden")
        self.__lengte = lengte
        return self.__lengte

    def GC(self):
        """Berekent het GC percentage van de sequentie
        """
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        n = seq.count("N")
        tot = a+t+c+g+n
        lengte = len(seq)
        if lengte == tot:
            GcPer = (g+c) / tot * 100
            print("Het GC percentage is: ", GcPer, "%")
        else:
            print("DNA bestaat alleen uit ACTGN")
        self.__gcp = GcPer
        return self.__gcp

def deel2():
    """Opent een fasta bestand en split deze in headers en sequenties. Hierna word het GC percentage,
    de lengte en de bijbehorende RNA sequenties berekend
    """
    bestand = open("Felis_catus.Felis_catus_8.0.cdna.all.fa", "r")
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)

    gc = []
    for i in range(len(headers)):
        a = seqs[i].count("A")
        t = seqs[i].count("T")
        c = seqs[i].count("C")
        g = seqs[i].count("G")
        n = seqs[i].count("N")
        lengte = len(seqs[i])
        tot = a+t+c+g+n
        GcPer = (g + c) / tot * 100
        gc.append(GcPer)
        #print(headers[i], ":", GcPer, "%")
        #print(headers[i], "is", lengte, "nucleotiden lang")

    RNA = []
    for i in range(len(seqs)):
        RNA.append(seqs[i])

    for i in range(len(RNA)):
        RNA[i] = RNA[i].replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
        #print("Het RNA van: ", headers[i], " is ", RNA[i])


deel2()