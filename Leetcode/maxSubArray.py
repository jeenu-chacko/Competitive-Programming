class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        totalSum = 0
        maximum = nums[0]
        for i in nums:
            totalSum = totalSum + i
            
            if totalSum > maximum:
                maximum = totalSum
            if totalSum < 0:
                totalSum = 0
        return maximum