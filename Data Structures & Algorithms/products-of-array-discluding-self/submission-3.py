class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        res = []
        count = 0

        while count < (len(nums)):
            currentOut = 1
            for i in range(len(nums)):
                if count == i:
                    continue
                currentOut *= nums[i]
            res.append(currentOut)
            count += 1
        
        return res



        
                