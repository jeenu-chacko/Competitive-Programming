class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def sub(temp,index): 
            if index  == len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[index])
            sub(temp,index+1)
            temp.pop()
            
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            sub(temp,index+1)
        sub([],0)    
        return res
        
        