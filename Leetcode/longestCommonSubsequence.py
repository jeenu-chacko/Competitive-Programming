class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1 = len(text1) - 1
        n2 = len(text2) - 1
        hashMap = dict()
        
        def commonSub(n1,n2):
            print(hashMap)
            if n1 < 0 or n2 < 0:
                return 0
            key = (n1,n2)
            if key not in hashMap:
                if text1[n1] == text2[n2]:
                    hashMap[key] = 1 + commonSub(n1 - 1, n2 - 1)
                    return hashMap[key]
                else:
                    hashMap[key] = max(commonSub(n1, n2 -1),commonSub(n1 - 1 , n2))
                    return hashMap[key]
            else:
                return hashMap[key]
            
        return commonSub(n1,n2)
        