from data import Data, Library, sortLibraries
from readfile import readfile

if __name__ == "__main__":
    day = 0
    readfile("data/a_example.txt")
    sortLibraries()

    print(Data.libraries[0].books)
    Data.libraries[0].sortBooks()
    print(Data.libraries[0].books)

