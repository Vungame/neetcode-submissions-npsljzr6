class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        count = 0

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        while count < k: 
            max_key = max(freq, key=freq.get)
            res.append(max_key)
            del freq[max_key]
            count += 1
        return res


