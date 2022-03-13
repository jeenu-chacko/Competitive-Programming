class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.strip()
        right = len(s) - 1
        left = len(s) - 1
        countChar = 0
        countSpace = 1
        while right > -1 :
            
            if s[right] != " ":
                right -= 1
                countChar = 1 
                countSpace = 0
            elif countSpace == 0:
                countSpace = 1
                res = res + s[right+1:left + 1] + " "
                left = right - 1
                right -= 1
            else:
                right -= 1
                left -= 1
                
        if left != right:
            res = res + s[0:left+1]
            
        return res
                
                