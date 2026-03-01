from typing import List

# Solution 1 - 100% runtime and 100% memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i = i+1
                j = j-1
        return True
    # Time complexity - O(n)
    # Space complexity - O(1)

# s = "Was it a car or a cat I saw?"
# print(isPalindrome(s))