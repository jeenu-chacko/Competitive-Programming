def getNthFib(n):
	fibArray=[0,1]
	counter=3
	while counter<=n:
		nextFib=fibArray[0]+fibArray[1]
		fibArray[0]=fibArray[1]
		fibArray[1]= nextFib
		counter+=1
	return fibArray[1] if n>1 else fibArray[0]
