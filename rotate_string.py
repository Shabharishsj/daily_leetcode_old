class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        l = len(s)
        
        for i in range(l):
            if s[-i:]+s[:l-i] == goal:
                return True
        
        return False
        