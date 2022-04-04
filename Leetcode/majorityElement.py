class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = 0
        currElement = 0
        for num in nums:
            if counter == 0:
                currElement = num
                counter += 1
            elif num == currElement:
                counter += 1
                
            else:
                counter -= 1
                
        return currElement
                