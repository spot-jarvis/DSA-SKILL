class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mpp = {}
        k = len(s1)
        for char in s1:
            mpp[char] = mpp.get(char,0)+1
        
        left = count = 0
        for right in range(len(s2)):
            if (right - left +1) > k :
                if s2[left] in mpp:
                    mpp[s2[left]] +=1
                    if mpp[s2[left]] > 0:
                        count -=1
                left +=1

            if s2[right] in mpp:
                mpp[s2[right]] -=1
                if mpp[s2[right]] >= 0:
                    count +=1
            
            if count == k:
                return True
        return False
