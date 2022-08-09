class Solution:
    def toLowerCase(self, s: str) -> str:
        
        temp = []
        
        
        for i in s:
            
            if ord(i) >= 65 and ord(i) <= 90:
                temp.append(chr(ord(i)+32))
            else:
                temp.append(i)
                
        return "".join(temp)
            
            