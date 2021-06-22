def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	l_one,l_two=0,0
	diff =float("inf")
	pair=[]
	while(l_one<len(arrayOne)) and l_two<len(arrayTwo):
		if(abs(arrayOne[l_one]-arrayTwo[l_two])<diff):
			diff=abs(arrayOne[l_one]-arrayTwo[l_two])
			pair[0:2]=arrayOne[l_one],arrayTwo[l_two]
			
		if(arrayOne[l_one]>arrayTwo[l_two]):
			l_two+=1
		else:
			l_one+=1
	return pair
		
		
	
