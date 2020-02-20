
class Data:
    nBooks = 0
    nLibraries = 0
    nScanningDays = 0
    bookScores = []
    libraries = []

class Book:
    def __init__(self, idf, score):
        self.idf = idf
        self.score = score

    def score(self):
        return self.score

    def __str__(self):
        return "Book(" + str(self.idf) + ", " + str(self.score) + ")"

    def __repr__(self):
        return self.__str__()

class Library:
    def __init__(self, nBooks, signupTime, nShipPerDay):
        self.nBooks = nBooks
        self.signupTime = signupTime
        self.nShipPerDay = nShipPerDay
        self.books = []

    def score(self):
        alpha = 1
        beta = 0.5
        gamma = 1
        return (
            pow(self.nShipPerDay, alpha) *
            pow(self.sumOfBookScores(), beta)
            ) / pow(self.signupTime, gamma)

    def sumOfBookScores(self):
        total = 0
        for book in self.books:
            total += Data.bookScores[book.idf]
        return total

    def sortBooks(self):
        self.books = sorted(self.books, key=Book.score, reverse=True)

def sortLibraries():
    Data.libraries = sorted(Data.libraries, key=Library.score, reverse=True)

