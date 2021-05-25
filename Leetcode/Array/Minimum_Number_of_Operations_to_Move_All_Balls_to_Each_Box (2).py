class Solution:    
    def minOperations(self, boxes: str) -> List[int]:
        left =0
        right =0
        count=0
        result=[0]*len(boxes)
        for i in range(0,len(boxes)):
            if(boxes[i]=='1'):
                right+=1
                count=count+i
        
         
        for i in range(0,len(boxes)):
                result[i]=count
                if(boxes[i]=='1'):
                    left+=1
                    right-=1
                count = count-(right+left)
                
        return result      
        