class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            leftSum = 0
            rightSum = 0
            
            for j in range(i):
                leftSum += nums[j]
                
            for j in range(i+1,len(nums)):
                rightSum += nums[j]
                
            if leftSum == rightSum:
                return i
        return -1
            

# other method


