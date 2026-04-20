class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
            else:
                return True

        return False


