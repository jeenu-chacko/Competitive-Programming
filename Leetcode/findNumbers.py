class Solution:
    def findNumber(self,nums):
        count=0

        for i in nums:
            digits=0
            while(i):
                i=i//10
                digits+=1
            if(digits%2==0):
                count+=1
        return count