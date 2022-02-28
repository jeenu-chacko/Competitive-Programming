class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d=set()
        
        for i in arr:
            if i*2 in d or i/2 in d:
                return True
            else:
                d.add(i)
        return False