class Solution:
    def myAtoi(self, s: str) -> int:
        result,sign = 0,1
        minimum,maximum = -2**31,2**31-1
        i,n = 0, len(s)

        while i < n and s[i] == " ":
            i+=1

        if i< n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i+=1
        while i<n  and s[i].isdigit():
            result = result * 10 +int(s[i])
            i+=1
        
        if result*sign < minimum : return minimum
        if result *sign > maximum : return maximum

        return result*sign