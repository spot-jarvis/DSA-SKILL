class Solution:
    def myAtoi(self, s):
        # Code here
        n = len(s)
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        i =0
        sign = 1
        while i <= n and s[i] == " ":
            i+=1
            
        if i <= n and s[i] =='+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i+=1
            
        while i<n and s[i].isdigit():
            res = res*10 +int(s[i])
            i+=1
            
        
        if res * sign < INT_MIN :
            return INT_MIN
        if res* sign > INT_MAX:
            return INT_MAX
        
        return res*sign
