class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def combination(index,curr,total):
            
            if total == target:
                res.append(curr.copy())
                return
            if total > target or index > len(candidates) - 1 or total < 0:
                return
            
            curr.append(candidates[index])
            combination(index, curr, total+candidates[index])
            curr.pop()
            combination(index+1,curr,total)
        combination(0,[],0)
        return res