def firstDuplicateValue(array):
	
    for i in range(len(array)):
		index = abs(array[i] )-1
		if array[index] < 0:
			return index + 1
		array[index] =  -1 *(array[index])
		
    return -1
