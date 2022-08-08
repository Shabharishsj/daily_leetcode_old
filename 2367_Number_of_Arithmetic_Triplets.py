class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        count = 0
        temp = set()
        
        for i in nums:
            
            if (i - diff in temp) and (i - diff * 2 in temp):
                count += 1
            temp.add(i)
            
        return count
        