class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        while (i < len(arr) and  (i + 1 ) < len(arr)):
            if (arr[i]>=arr[i+1]):
                break
            i += 1
        if i == len(arr)-1 or i==0:
            return False
        
        while (i < len(arr) and (i + 1 ) < len(arr)):
            if (arr[i+1] >= arr[i]):
                return False
            i=i+1
     
        return i==len(arr)-1
                