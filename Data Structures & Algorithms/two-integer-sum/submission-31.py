class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i, n in enumerate(nums):
            differences[n] = i

        for i, n in enumerate(nums):
            diff = target - n

            if diff in differences and differences[diff] != i:
                return [i, differences[diff]]
            
        return []
            
