def longestPeak(array):
	longestPeakLength = 0
	i = 1
	if len(array) < 3:
		return 0
	while i < len(array) - 1:
		
		if array[i - 1] < array[i] and array [i] > array[i + 1]:
			leftIndx = i - 1
			rightIndx = i + 1
			while leftIndx - 1 >= 0 and array[leftIndx - 1] < array[leftIndx]:
				leftIndx -= 1
			while rightIndx + 1 < len(array) and array[rightIndx + 1] < array[rightIndx]:
				rightIndx += 1
			
			longestPeakLength = max(longestPeakLength, (rightIndx  - leftIndx + 1))
			i = rightIndx
		else:
			i += 1
			
	return longestPeakLength