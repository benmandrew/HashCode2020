
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
        for book in self.bookSet:
            total += Data.bookScores[book]
        return total
