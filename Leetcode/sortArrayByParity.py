class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        for r in range(0,len(nums)):
            
            if nums[r] %2 == 0:
                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
        return nums
        