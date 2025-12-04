class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = ""
        for char in s :
            if char == "(":
                if depth > 0 :
                    result += char
                depth += 1
            else :
                depth -=1
                if depth > 0 :
                    result += char 
        return result 