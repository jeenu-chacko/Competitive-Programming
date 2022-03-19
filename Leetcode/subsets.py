class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def sub(nums,temp,index):
            
            if index == len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[index])
            sub(nums,temp,index+1)
            
            temp.pop()
            sub(nums,temp,index+1)
        sub(nums,[],0)    
        return res
        