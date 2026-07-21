class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = set()

        for n in nums:
            if n not in dup:
                dup.add(n)
            else:
                return n