# Read a list of integers from the user
readList = []
exitWord = "exit"
inputString = ""
while True: # Infinite Loop
	inputString = input("Please enter an integer, or \"exit\" to stop: ")
	if inputString == exitWord:
		break # Exit the loop
	else:
		try:
			inputValue = int(inputString)
		except ValueError:
			continue # Skip next lines if number is not integer
		readList.append(inputValue)

# Find all pairs of numbers (a,b) where a*b is even, a+b is odd
pairsList = []
for index in range(len(readList)):
	for mark in range(index+1, len(readList)):
		if ((readList[index] + readList[mark]) % 2 == 1) and ((readList[index] * readList[mark]) % 2 == 0):
			pairsList.append( (readList[index], readList[mark]) )

# Print out a formatted list of the pairs
print("From your inputted numbers, the following pairs have an even product, and an odd sum: ", end='')
for index in range(len(pairsList)):
	if index % 10 == 0:
		print("\n", end = '')

	if index == (len(pairsList)-1):
		print(str(pairsList[index]))
	else:
		print(str(pairsList[index]) + ", ", end='')
