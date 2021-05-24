class Solution:    
    def minOperations(self, boxes: str) -> List[int]:
        
        boxesarr= [int(x) for x in boxes]
        answer=[0]*len(boxesarr)
        for x in range(0,len(boxesarr)):
            steps=0
            for y in range(0,len(boxesarr)):
                
                if(boxesarr[y]==1):
                    steps=steps+abs(y-x)
            answer[x]=steps
        return answer
        
        
                
                
        
        