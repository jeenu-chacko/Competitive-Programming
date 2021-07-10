class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        
        num=nums[0]
        res=[]
        perms=self.permute(nums[1:])
        for perm in perms:
            for i in range(len(nums)):
                res.append(perm[:i]+[num]+perm[i:])
        return res


