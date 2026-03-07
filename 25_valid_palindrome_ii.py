from typing import List

# Solution 1 - 100% memory and 99.94% memory
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i+=1
                    j-=1
            return True
        i = 0
        j = len(s)-1

        while i<j:
            if s[i] != s[j]:
                return (is_palindrome(i+1, j) or is_palindrome(i, j-1))
            i+=1
            j-=1
        return True
    # Time complexity: O(n)
    # Space complexity: O(1)