class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = ""
        left = 0
        
        right =1
        
        while left <= right and right < len(s):
            
            if s[right] == " ":
                temp = s[left:right]
                res = res + temp[::-1] + " "
                left = right + 1
                right += 1
            else:
                right = right + 1
                
        if left != right:
            print("hai")
            temp = s[left:right]
            res = res + temp[::-1]
        
        return res