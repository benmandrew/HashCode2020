from data import Data, Library, sortLibraries
from readfile import readfile
from simulate import Running, simulate

if __name__ == "__main__":
    fileNames = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
    for fileName in fileNames:
        
        Data.nBooks = 0
        Data.nLibraries = 0
        Data.nScanningDays = 0
        Data.bookScores = []
        Data.libraries = []
        
        Running.currentProcessing = None  # The current library being processed
        Running.daysLeft = 0  # How many days are left for the current library to be processed
        Running.librariesLeft = []  # The libraries still to be processed
        Running.processed = []  # Librarues that have been processed
        Running.numberProcessed = 0
        Running.totalScore = 0  # The total score
        
        
        readfile("data/{}".format(fileName))
        sortLibraries()
        for lib in Data.libraries:
            lib.sortBooks()
        print("Read/sort files")

        simulate(
            Data.libraries,
            Data.nScanningDays,
            "out/out_{}.txt".format(fileName[0]))
