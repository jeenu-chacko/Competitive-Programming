def isValidSubsequence(array, sequence):
	indexOfs=0
	for a in array:
		if a==sequence[indexOfs]:
			indexOfs+=1
		if (indexOfs==len(sequence)):
			return True
	return False
