class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mpp = {'}':'{' ,']':'[',')':'('}

        for char in s:
            if char in mpp:
                top = stack.pop() if stack else '#'
                if top != mpp[char]:
                    return False
            else:
                stack.append(char)
        return not stack
