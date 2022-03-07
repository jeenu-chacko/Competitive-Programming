def arrayOfProducts(array):
	res = []
	product = 1
	for i in array:
		res.append(product)
		product = product * i
	
	product = 1
	for i in range(len(array)-1,-1,-1):
		res[i] = res[i] * product
		product = product * array[i]
		
	return res