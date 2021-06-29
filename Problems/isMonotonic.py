def isMonotonic(a):
	
	asc=True
	desc=True
	for i in range(len(a)-1):
		if(a[i]>a[i+1]):
			asc=False
		elif(a[i]<a[i+1]):
			desc=False
	return asc or desc
