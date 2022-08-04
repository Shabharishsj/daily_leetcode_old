class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        nums1 = nums[:n]
        nums2 = nums[n:]
        
        result = []
        
        for x,y in zip(nums1,nums2):
            result.append(x)
            result.append(y)
        
        return result