class Solution:
    def spiralOrder(self, array: List[List[int]]) -> List[int]:
       
        if not array:
                return []
        res=[]
        rowStart,rowEnd=0,len(array)-1
        colStart,colEnd=0,len(array[0])-1

        while(rowStart<=rowEnd and colStart<=colEnd):

            for i in range(colStart,colEnd+1):
                res.append(array[rowStart][i])

            for j in range(rowStart+1,rowEnd):
                res.append(array[j][colEnd])

            if rowEnd+1 != rowStart+1:
                for i in range(colEnd,colStart-1,-1):
                    res.append(array[rowEnd][i])

            if(colStart != colEnd):
                for j in range(rowEnd-1,rowStart,-1):
                    res.append(array[j][colStart])

            colStart+=1
            rowStart+=1
            colEnd-=1
            rowEnd-=1
        return res
