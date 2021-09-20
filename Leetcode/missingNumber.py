class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res=0
        for i in range(0,len(nums)):
            res=res^nums[i]^i
        
        return res^len(nums)
        
