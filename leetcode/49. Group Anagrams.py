"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

#Time Limit Exceeded
"""class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = dict()
        strs = sorted(strs)
        anagrams[tuple(sorted(strs[0]))] = [strs[0]]
        for st in range(1,len(strs)):
            found = False
            for key in list(anagrams):
                x = strs[st]
                if  tuple(sorted(x)) == key:
                    anagrams[key].append(str(strs[st]))
                    found = True
            
            if found == False:    
                anagrams[tuple(sorted(strs[st]))] = [strs[st]]
        return anagrams.values()"""

from collections import defaultdict

#Claims 63ms of running 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        
        return anagrams.values()        
    
s = Solution()
input = ["eat","tea","tan","ate","nat","bat"]
print(f'solution is {s.groupAnagrams(input)}')
