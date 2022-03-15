class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        right = len(s) - 1
        index = 0
        if len(s)==0:
            return True
        for i in t:
            if i == s[index] and index < (right + 1):
                index += 1
            if index-1 == right:
                return True
        return False