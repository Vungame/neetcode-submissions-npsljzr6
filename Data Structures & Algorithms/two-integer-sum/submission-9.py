class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dup = {}

        for i, j in enumerate(nums):
            dup[j] = i

        for i, j in enumerate(nums):
            diff = target - j
            if diff in dup and dup[diff] != i:
                return [i, dup[diff]]

        return []
                
