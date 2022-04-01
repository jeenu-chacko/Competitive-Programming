
def maximumNonAdjacentSum(nums): 
    n = len(nums)-1
    print( maximumSum(n,0,nums))
def maximumSum(index,nums):
    if index == 0:
        return nums[index]
    if index < 0:
        return 0
    pick = nums[index] + maximumSum(index-2, nums)
    notpick = 0 + maximumSum(index-1,nums)
    return max(pick,notpick)
	



maximumNonAdjacentSum([1,2,4,5])