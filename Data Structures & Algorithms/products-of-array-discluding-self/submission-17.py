class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        res = []
        i = 0

        while i < len(nums):
            j = 0
            num = 1
            while j < len(nums):
                if i != j: 
                    num *= nums[j]
                j += 1
            res.append(num)
            i += 1
        
        return res




        


                



        
                