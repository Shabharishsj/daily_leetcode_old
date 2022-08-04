class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        summ = ""
        
        for i in address:
            
            if i == ".":
                i = "[.]"
            
            summ += i
            
        return summ