class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        firstMaximum = -1
        secondMaximum = -1
        for i in nums:
            if firstMaximum == i or secondMaximum == i:
                continue
            if firstMaximum < i:
                print("hai")
                secondMaximum = firstMaximum
                firstMaximum = i
            elif i > secondMaximum:
                secondMaximum = i
        if firstMaximum >= secondMaximum * 2:
            return nums.index(firstMaximum)
        return -1