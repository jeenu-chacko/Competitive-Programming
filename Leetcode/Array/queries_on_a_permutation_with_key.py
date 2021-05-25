class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr=[i for i in range(1,m+1)]
        result=[0]*len(queries)
        
        for i in range(0,len(queries)):
            query=queries[i]
            j=arr.index(query)
            result[i]=j
            arr.remove(query)
            arr=[query]+arr
                
        return result
        
        