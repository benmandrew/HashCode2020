from data import Data, Library, sortLibraries
from readfile import readfile
from simulate import Running, simulate

if __name__ == "__main__":
    readfile("data/c_incunabula.txt")
    sortLibraries()

    for lib in Data.libraries:
        lib.sortBooks()

    simulate(
        Data.libraries, Data.nScanningDays)
    
    
