class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        cnt = 0

        while i >= 0 and s[i] == " ":
            i-=1
        
        while i >=0 and s[i] != " ":
            cnt +=1
            i-=1
        
        return cnt
    
# one line solving 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.split().pop())