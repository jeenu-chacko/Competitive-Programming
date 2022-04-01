def lcs(str1, str2):
    n1 = len(str1) - 1
    n2 = len(str2) - 1
    lookup = dict()

    def commonSubstring(n1,n2,ans):
        if n1 < 0 or n2 < 0:
            return 0
        key = (n1,n2)
        
        if key not in lookup:
            if str1[n1] == str2[n2]:
                lookup[key] = 1 + commonSubstring(n1-1 , n2-1,ans)
                ans = max(ans,lookup[key])
       
                return ans
            else:
            	lookup[key] = 0
            	return lookup[key]
        else:
        	return lookup[key]
    return commonSubstring(n1,n2,0)

    print(lookup)

    
            
    
    
# 	commonSubstring(n1, n2)
        
lcs("ba","ba")    