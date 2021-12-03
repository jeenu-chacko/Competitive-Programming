class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(numbers):
            if num in d:
                return [d[num],i+1]
            d[target-num]=i+1
