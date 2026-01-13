class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        letters = []
        result = []
        for word in strs:
# we cant sort the string thats why we converted these into list 
            letters = list(word)
            letters = sorted(letters)
#for joining the list words into the string
            key = "".join(letters)


            if key not in freq:
                freq[key] = []
            freq[key].append(word)

        for key ,value in freq.items():
            result.append(value)
        return result
#Revised 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
         freq = {}
         result = []
         for word in strs:
             letters = list(word)
             letter = sorted(letters)
             key = "".join(letter)
             if key not in freq:
                 freq[key] = []
             freq[key].append(word)

        
         for key,value in freq.items():
             result.append(value)
         return result