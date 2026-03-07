from typing import List

# Solution 1 - 100% runtime and 93.7% memory
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        res = ""
        while i<len(word1) and j<len(word2):
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        res+=word1[i:]
        res+=word2[j:]
        return res