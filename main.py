from data import Data, Library, sortLibraries
from readfile import readfile
from simulate import Running, simulate

if __name__ == "__main__":
    fileName = "c_incunabula.txt"
    readfile("data/{}".format(fileName))
    sortLibraries()
    for lib in Data.libraries:
        lib.sortBooks()
    print("Read/sort files")

    simulate(
        Data.libraries,
        Data.nScanningDays,
        "out_{}.txt".format(fileName[0]))
    
    
