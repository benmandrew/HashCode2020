from data import Data, Library, Book

def readfile(name):
    lines = []
    with open(name, "r") as f:
        lines = f.readlines()
    top = lines[0].strip().split(" ")
    Data.nBooks = int(top[0])
    Data.nLibraries = int(top[1])
    Data.nScanningDays = int(top[2])
    for e in lines[1].strip().split(" "):
        Data.bookScores.append(int(e))

    for l in lines[2::2]:
        lf = l.strip().split(" ")
        if lf[0] == '':
            continue
        lib = Library(int(lf[0]), int(lf[1]), int(lf[2]))
        Data.libraries.append(lib)
    
    for i, l in enumerate(lines[3::2]):
        lf = l.strip().split(" ")
        for e in lf:
            b = Book(int(e), Data.bookScores[int(e)])
            Data.libraries[i].books.append(b)
