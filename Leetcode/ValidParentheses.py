class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        res=[]
        for i in s:
            if i in ('(','[','{'):
                res.append(i)
            elif not res or (res.pop(),i) not in (('(',')'),('{','}'),('[',']')):
                    return False

        return not res       
                 
                    
