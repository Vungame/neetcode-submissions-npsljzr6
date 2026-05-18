class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} 

        for i, n in enumerate(nums):
            diff[n] = i

        for i, n in enumerate(nums):
            difference = target - n
            if difference in diff and diff[difference] != i:
                return [i, diff[difference]]
        return []


     


        
        