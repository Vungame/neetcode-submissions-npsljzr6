class Solution:
    def findMin(self, nums: List[int]) -> int:
        current = nums[0]
        for i in nums[1::]:
            if i < current:
                current = i
        
        return current
