class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        mapy = {' ':' '}
        letters = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        i = 0
        
        
        for l in key:
            if l not in mapy:
                mapy[l] = letters[i]
                i += 1
                
            if len(mapy) == 27:
                break
            
        
        for k in message:
            result += mapy[k]
            
        
        return result 