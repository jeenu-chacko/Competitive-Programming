class Solution:
    def findMaxConsecutiveOne(self,nums:List[int])->int:
        count = 0
        i=0
        maximum=0

        while(i<len(nums)):
            if nums[i]==1:
                count+=1
                maximum=max(maximum,count)
            else:
                count=0
            i=i+1
        return maximum
