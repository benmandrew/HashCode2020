from data import removeBookFromAllLibraries

class Running:
    currentProcessing = None  # The current library being processed
    daysLeft = 0  # How many days are left for the current library to be processed
    librariesLeft = []  # The libraries still to be processed
    processed = []  # Librarues that have been processed
    numberProcessed = 0
    totalScore = 0  # The total score



def simulate(libraries, D, outFileName):
	# ASSUMPTION: libraries is already sorted from best to worst
	Running.librariesLeft = libraries
	libForOutput = []  # list of LibrarySection objects -- used for building output
	finishedProcessing = False

	for d in range(D):
		# Stuff for processing libraries
		if Running.daysLeft <= 0 and not finishedProcessing:
			print("{} libraries left. {}/{} days".format(len(libraries), d, D))
			# Add next library
			if Running.currentProcessing is not None:
		
				nBooksFromLibrary = (D - d) * Running.currentProcessing.nShipPerDay
				if nBooksFromLibrary <= len(Running.currentProcessing.books):
					Running.currentProcessing.scanned = Running.currentProcessing.books[:nBooksFromLibrary]
				else:
					Running.currentProcessing.scanned = Running.currentProcessing.books
				Running.processed.append(Running.currentProcessing)
				libForOutput.append(Running.currentProcessing)
			Running.numberProcessed += 1

			if len(Running.librariesLeft) > 0:
				Running.currentProcessing = Running.librariesLeft.pop(0)
				Running.daysLeft = Running.currentProcessing.signupTime
			else:
				finishedProcessing = True
		# Decrement the days left for the current library
		Running.daysLeft -= 1

	# adding data into output file
	outputFile = open(outFileName, "w")
	outputFile.write("{}\n".format(len(Running.processed)))  # add nº of libraries processed
	# add section for each library int the output file
	for lib in libForOutput:
		line1 = "{} {}\n".format(lib.idx, len(lib.scanned))
		line2 = ""

		for thisBook in lib.scanned:
			line2 = line2 + "{} ".format(thisBook.idf)

		outputFile.write(line1)
		outputFile.write(line2 + "\n")
