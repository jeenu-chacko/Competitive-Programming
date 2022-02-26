def sortedSquaredArray(array):
    sorted_array = [0] * len(array)
	
	r = len(array)-1
	left=0
	right = len(array) - 1
	while r >= 0:
		if abs(array[left]) > abs(array[right]):
			sorted_array[r] = array[left] * array[left]
			r = r - 1
			left = left + 1
		else:
			sorted_array[r] = array[right] * array[right]
			right = right -1
			r -= 1
				
    return sorted_array