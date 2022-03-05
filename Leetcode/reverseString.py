class Solution:
   
    def reverseString(self,s):
        if len(s)==0:
            return s
        return self.reverseString(s[1:]) + [s[0]]
soln = Solution()
print(soln.reverseString(["h","e","l","l","o"]))
