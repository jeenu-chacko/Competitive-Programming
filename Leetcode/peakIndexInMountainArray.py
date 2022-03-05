class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 1
        if len(arr) < 3:
            return 0
        
        while i < len(arr):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i
            i += 1