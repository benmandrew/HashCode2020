class Running:
	currentProcessing = None #The current library being processed
	daysLeft = 0 #How many days are left for the current library to be processed
	librariesLeft = [] #The libraries still to be processed
	processed = [] #Librarues that have been processed
	numberProcessed = 0
	totalScore = 0 #The total score

def simulate(D):

	for d in range(D):
		#Stuff for processing libraries
		if(Running.daysLeft <= 0 and len(Running.librariesLeft) > 0):
			#Add next library
			Running.processed.add(Running.currentProcessing)
			Running.numberProcessed += 1
			Running.currentProcessing = Running.librariesLeft.pop(0)
			Running.daysLeft = Running.currentProcessing.signupTime
		#Decrement the days left for the current library
		Running.daysLeft -= 1

		#Stuff for processing books
		for l in Running.processed:
			for i in range(l.nShipPerDay):
				if(len(l.books) > 0):
					popped = l.books.pop()
					l.scanned.add(popped)
					RunningtotalScore += popped.score


