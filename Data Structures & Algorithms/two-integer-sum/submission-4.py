class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, j in enumerate(nums):
            diffs[j] = i
        
        for i, j in enumerate(nums):
            difference = target - j
            if difference in diffs and diffs[difference] != i: 
                return [i, diffs[difference]]

    