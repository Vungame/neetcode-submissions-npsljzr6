class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # 2
        for i in range(len(nums)):
            res += i - nums[i]
            #2 + 0
            #2 + -1 = 1

        return res 