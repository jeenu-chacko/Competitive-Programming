class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        array= [[0 for j in range(n)] for i in range(n)]
        
        if not n:
            return []
        
        ele=0
        rowStart=0
        colStart=0
        colEnd=n-1
        rowEnd=n-1
        
        

        while(rowStart<=rowEnd and colStart<=colEnd):

            for i in range(colStart,colEnd+1):
                ele+=1
                array[rowStart][i]=ele
                
                

            for j in range(rowStart+1,rowEnd):
                ele+=1
                print(ele)
                array[j][colEnd]=ele

            if rowEnd+1 != rowStart+1:
                for i in range(colEnd,colStart-1,-1):
                    ele+=1
                    array[rowEnd][i]=ele

            if(colStart != colEnd):
                for j in range(rowEnd-1,rowStart,-1):
                    ele+=1
                    array[j][colStart]=ele

            colStart+=1
            rowStart+=1
            colEnd-=1
            rowEnd-=1
        return array
        
