class Solution:
    def countAsterisks(self, s: str) -> int:
        
        result = ""
        
        flag = True
        
        for i in s:
            
            if i == '|':
                flag = not flag
                
            if flag:
                result += i
                
        
        count = 0
        
        for j in result:
            if j == "*":
                count += 1
        
        return count