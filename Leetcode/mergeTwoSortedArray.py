class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l1 , l2 = 0 , 0
        
        while l1 < m and l2 < n:
            
            if nums1[l1] <= nums2[l2]:
                l1 += 1
            else:
                temp = nums1[l1]
                nums1[l1] = nums2[l2]
                nums2[l2] = temp
                nums2.sort()
                l1 += 1
        
            
        while l2 < n:
            nums1[l1] = nums2[l2]
            l2 += 1
            l1 += 1