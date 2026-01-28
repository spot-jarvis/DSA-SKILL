class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        res = len(t)

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                res -=1
                j+=1
            i +=1
        return res
"""
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
"""