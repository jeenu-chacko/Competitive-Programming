class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum = None
        secondMaximum = None
        thirdMaximum = None
        count =0
        if len(nums) < 3:
            return max(nums)
        
        for num in nums:
         
            if num == maximum or num == secondMaximum or num ==  thirdMaximum:
                continue
                
            if maximum == None or num > maximum:
                thirdMaximum = secondMaximum
                secondMaximum = maximum
                maximum = num

                count += 1
            elif  secondMaximum == None or num > secondMaximum:
                thirdMaximum = secondMaximum
                secondMaximum = num

                count += 1
            elif thirdMaximum == None or num > thirdMaximum:
                thirdMaximum = num
                count += 1

        
        if thirdMaximum != None:
            return thirdMaximum
        return maximum
                