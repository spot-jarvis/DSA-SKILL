#These is a brute force approach having time complexity O(n^2)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        left ,right = 0,len(cleaned)-1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
# in below the optimal approach 
#we use two pointer technique to solve these there is some edge cases too so we have to solve that too
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0,len(s)-1
        while left < right:
            while  left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1
        return True
# by these we can automatically check and remove the spaces and other char 
