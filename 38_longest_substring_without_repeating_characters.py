from typing import List
# Solution 2 - 100% runtime and 100% memory
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index:
                left = max(left, char_index[s[right]] + 1)

            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len

# Solution 1 - 100% runtime and 100% memory
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_map = [False]*95 # 95 for all printable ASCII characters
        left=0
        right=0
        max_len=0
    # Time complexity - O(n)
    # Space complexity - O(m)

        while right<len(s):
            while char_map[ord(s[right])-ord("!")] == True: # ! for the start of 95 ASCII printable characters
                char_map[ord(s[left])-ord("!")] = False
                left+=1
            char_map[ord(s[right])-ord("!")] = True
            max_len = max(max_len, right-left+1)
            right+=1
        return max_len
    # Time complexity - O(n)
    # Space complexity - O(m)

# s = "zxyzxyz"
# expected=3
# s = "xxxx"
# expected=1
# s = "zyxyz"
# expected = 3