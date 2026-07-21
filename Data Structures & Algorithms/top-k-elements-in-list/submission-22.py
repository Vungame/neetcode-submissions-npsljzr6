class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #Need to do +1 since its 0 to n buckets, not 1 to n buckets

        for num in nums:
            count[num] = 1 + count.get(num, 0) #Makes the count hashmap, the corresponds the (nums element : # of times it appeared) 

        for num, cnt in count.items():
            freq[cnt].append(num) 


        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

            