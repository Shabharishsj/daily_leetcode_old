class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split()
        
        D = {}
        
        for i in s:
            n = int(i[-1])
            last = len(i)-1
            i = i[:last]
            
            D[n] = i
            
        
        result = []
        
        for x in range(1,len(D)+1):
            
            result.append(D[x])
            
        
        return " ".join(result)
            