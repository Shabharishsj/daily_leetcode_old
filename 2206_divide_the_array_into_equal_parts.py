class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        seen = set()
        
        for x in nums:
            if x in seen:
                seen.discard(x)
            else:
                seen.add(x)
                
        
        return not seen 
        