class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        res = 0

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for key, values in freq.items():
            if values == 1:
                res = key
        
        return res
