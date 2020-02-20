class LibrarySection:
    def __init__(self, idx):
        self.idx = idx
        self.numBooksScanned = 0
        self.books = []


outputFile = open("output.txt", "w")

outputFile.write("%d".format(len(processed)))

# build libForOutput in the simulation -- list of LibrarySection objects
# will add id f lib when init obj, then in each timestep incr nº of boks scanned and add book id to list of books
for libSect in libForOutput:
    line1 = "%d %d".format(libSect.idx, libSect.numBooksScanned)
    line2 = ""

    for thisBook in libSect.books:
        line2 = line2 + "%d ".format(thisBook.idf)

    outputFile.write(line1)
    outputFile.write(line2)
