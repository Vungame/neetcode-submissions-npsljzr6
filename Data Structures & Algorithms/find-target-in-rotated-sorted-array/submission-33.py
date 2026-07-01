class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(left: int, right: int):
            while left <= right:
                mid = (left + right) // 2 
                if nums[mid] == target: 
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        left_side = binary_search(0, pivot - 1)
        if left_side != -1:
            return left_side
        
        return binary_search(pivot, len(nums) - 1)



