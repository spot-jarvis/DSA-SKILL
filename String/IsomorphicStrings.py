class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mpp1 = {}
        mpp2 = {}
        for a , b in zip(s,t):
            if a in mpp1:
                if mpp1[a] != b:
                    return False
            else:
                mpp1[a] = b

            if b in mpp2:
                if mpp2[b] != a:
                    return False
            else:
                mpp2[b] = a
        return True