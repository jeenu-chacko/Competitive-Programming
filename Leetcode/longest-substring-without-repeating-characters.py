class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set=set()
        l=0
        r=0
        max_count=0
        while(r<len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
                
            char_set.add(s[r])
            r=r+1
            max_count=max(max_count,r-l)
            
        return max_count
                    
