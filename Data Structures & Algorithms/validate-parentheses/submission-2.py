class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {")" : "(", "]" : '[', "}" : "{"}

        for i in s:
            if i in closing:
                if stack and stack[-1] == closing[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
        
        return True if not stack else False
