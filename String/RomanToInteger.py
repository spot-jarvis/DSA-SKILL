class Solution:
    def romanToInt(self, s: str) -> int:
        Total_sum = 0
        roman = {
            'I' : 1,
            'V' :  5,
            'X' :  10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
         }
        i = 0
        while i < len(s):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                Total_sum += roman[s[i+1]] - roman[s[i]]
                i += 2
            else:
                Total_sum += roman[s[i]]
                i+=1
        return Total_sum