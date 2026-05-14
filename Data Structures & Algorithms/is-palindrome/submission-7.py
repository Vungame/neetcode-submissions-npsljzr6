class Solution:
    def isPalindrome(self, s: str) -> bool:
        curr = "".join(c for c in s if c.isalnum())

        left = 0
        right = len(curr) - 1

        while(left < right):
            if(curr[left].lower() == curr[right].lower()):
                left += 1 
                right -= 1
            else:
                return False
        return True

