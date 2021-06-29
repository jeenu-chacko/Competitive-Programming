def moveElementToEnd(array, toMove):
    s,e=0,len(array)-1
	while(s<e):
		if(array[s]==toMove and array[e]!=toMove):
			array[s],array[e]=array[e],array[s]
			s=s+1
			e=e-1
		elif(array[s]==toMove and array[e]==toMove):
			e=e-1
		else:
			s=s+1
		
	return array
