class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length,res,l=0,0,0
        charSet=set()
        if len(s)==1:
            return 1
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) 
                res=max(res,length)     
                l=l+1
                print(l,r)
            charSet.add(s[r])
            length=(r-l+1)
            res=max(res,length)
         
            
        return res
