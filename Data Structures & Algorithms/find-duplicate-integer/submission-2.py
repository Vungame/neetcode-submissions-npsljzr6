class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 

        #This while loop proves that their is a cycle
        while True:
            slow = nums[slow] #The slower pointer
            fast = nums[nums[fast]] #The fast pointer

            if slow == fast: 
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        
        
        

        
