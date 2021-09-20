class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,mid=0,0
        end=len(nums)-1
        
        while(mid<=end):
            
            if(nums[mid]==0):
                nums[l],nums[mid]=nums[mid],nums[l]
                mid+=1
                l+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                nums[end],nums[mid]=nums[mid],nums[end]
                end-=1
        return nums
