class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dup = set()
        start = []
        count = []

        for n in nums:
            dup.add(n)
        
        for i in range(len(nums)):
            current = nums[i] - 1 
            if current not in dup:
                start.append(current + 1)
        
        for n in start:
            cnt = 1
            while True:
                if n + 1 in dup:
                    cnt += 1
                    n += 1
                else: 
                    break
            count.append(cnt)
        
        return max(count) if count else 0
            
            

            
        






         