 #Solution 1 76 ms 90%
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magHash = {}
        for i in range(len(magazine)):
            if magazine[i] in magHash:
                magHash[magazine[i]] += 1
            else:
                magHash[magazine[i]] = 1
                
        for i in range(len(ransomNote)):
            if ransomNote[i] in magHash:
                if magHash[ransomNote[i]] > 0:
                    magHash[ransomNote[i]] -= 1
                else:
                    return False
            else:
                return False
        return True 
        
#78 ms runtime,  good memory usage,
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magHash = {"target" : len(ransomNote), "string": ""}
        ragHash = {}

        maxIter = len(ransomNote)
        if len(magazine) > len(ransomNote):
            maxIter = len(magazine)

        for i in range(maxIter):
            
            if magHash["target"] == 0:
                return True
            
            #Looking the char at target
            if i < len(ransomNote):
                if ransomNote[i] in magHash:
                    magHash[ransomNote[i]] += 1
                else:
                    magHash[ransomNote[i]] = 1
                    
                if ransomNote[i] in ragHash:
                    if ragHash[ransomNote[i]] > 0 and magHash[ransomNote[i]] > 0:
                        ragHash[ransomNote[i]] -= 1
                        magHash[ransomNote[i]] -= 1
                        magHash["target"] -= 1
                        

            #Looking the char at target
            if i < len(magazine):
                if magazine[i] in ragHash:
                    ragHash[magazine[i]] += 1
                else:
                    ragHash[magazine[i]] = 1
                    
                if magazine[i] in magHash:
                    if ragHash[magazine[i]] > 0 and magHash[magazine[i]] > 0:
                        ragHash[magazine[i]] -= 1
                        magHash[magazine[i]] -= 1
                        magHash["target"] -= 1
        return magHash["target"] == 0

# Youtube 62 ms runtime, 
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        
        for c in magazine: counter[c] += 1
                
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else: 
                counter[c] -= 1
                    
        return True

ransomNote = "acbva"
magazine = "vbbbbbcbbbbbabbbbbba"

s = Solution()
print(s.canConstruct(ransomNote, magazine))