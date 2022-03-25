class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n1 = len(s) - 1
        n2 = len(s) - 1
        s1 = s[::-1]
        lookup = dict()
        
        def palindrome(n1,n2):
            
            if n1 < 0 or n2 < 0 :
                return 0
            key = (n1,n2)
            if key not in lookup:
                if s[n1] == s1[n2]:
                    lookup[key] =  1 + palindrome(n1 - 1, n2 -1)
                    return lookup[key]
                lookup[key] = max(palindrome(n1,n2-1), palindrome(n1-1,n2))
                return lookup[key]
            return lookup[key]
        
    
        return palindrome(n1,n2)