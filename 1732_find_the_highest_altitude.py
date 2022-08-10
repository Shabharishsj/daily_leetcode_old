class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alt = 0
        maxy = 0
        
        for i in gain:
            alt += i
            
            if alt > maxy:
                maxy = alt
            
        return maxy