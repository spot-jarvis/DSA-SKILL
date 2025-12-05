class Solution:
    def largestOddNumber(self, num: str) -> str:
        number = int(num)
        while number != 0:
            if number % 2 != 0:
                return str(number)
            else:
                number = number//10
        return ""