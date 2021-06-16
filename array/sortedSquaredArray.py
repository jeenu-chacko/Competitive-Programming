def sortedSquaredArray(array):
    left =0
	right=len(array)-1
	x=-1
	arr=[0]*len(array)
	while(left<=right):
		if(abs(array[left])>abs(array[right])):
			arr[x]=array[left]**2
			left=left+1
		else:
			arr[x]=array[right]**2
			right=right-1
		x=x-1
    return arr
