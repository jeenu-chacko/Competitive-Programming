def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	pointerArrayOne = 0
	pointerArrayTwo = 0
	minimum = float("inf")
	res = []
	while pointerArrayOne < len(arrayOne) and pointerArrayTwo < len(arrayTwo):
		currMinimum = abs(arrayOne[pointerArrayOne] - arrayTwo[pointerArrayTwo])
		if currMinimum < minimum:
			minimum = currMinimum
			res= [arrayOne[pointerArrayOne],arrayTwo[pointerArrayTwo]]
		if arrayOne[pointerArrayOne] < arrayTwo[pointerArrayTwo]:
			pointerArrayOne += 1
		else:
			pointerArrayTwo +=1
	return res
	