
class Data:
    nBooks = 0
    nLibraries = 0
    nScanningDays = 0
    bookScores = []
    libraries = []

class Library:
    def __init__(self, nBooks, signupTime, nShipPerDay):
        self.nBooks = nBooks
        self.signupTime = signupTime
        self.nShipPerDay = nShipPerDay
        self.bookSet = set()

def readfile(name):
    lines = []
    with open(name, "r") as f:
        lines = f.readlines()
    top = lines[0].strip().split(" ")
    Data.nBooks = int(top[0])
    Data.nLibraries = int(top[1])
    Data.nScanningDays = int(top[2])
    for e in lines[1].strip().split(" "):
        Data.bookScores.append(e)

    for l in lines[2::2]:
        lf = l.strip().split(" ")
        if lf[0] == '':
            continue
        lib = Library(int(lf[0]), int(lf[1]), int(lf[2]))
        Data.libraries.append(lib)
    
    for i, l in enumerate(lines[3::2]):
        lf = l.strip().split(" ")
        for e in lf:
            Data.libraries[i].bookSet.add(int(e))