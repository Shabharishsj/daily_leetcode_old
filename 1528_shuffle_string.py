class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        D = {}
        
        s = list(s)
        
        for x,y in zip(s,indices):
            D[y] = x
            
        
        result = ""
        
        indices.sort()
        
        for l in indices:
            
            result += D[l]
            
        return result
