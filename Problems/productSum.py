def productSum(array,depth=1):
	sum=0
	for i in array:
		if type(i)==list:
			sum=sum+productSum(i,depth+1)
			print(depth)
		else:
			sum=sum+i
	return sum*depth
			
