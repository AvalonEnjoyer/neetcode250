from typing import List

# Solution 1 - 100% runtime and 100%
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        if n1 < n2:
            return ""
        char_map = [0]*58
        for char in t:
            char_map[ord(char)-ord('A')] += 1
        temp_map = [0]*58
        # Initialize the window
        left = 0
        count = 0
        min_window = float('inf')
        min_coords = (0, 0)
        for right in range(n1):
            key = ord(s[right])-ord('A')
            temp_map[key] += 1
            # If the character is in t update count
            if char_map[key] != 0 and temp_map[key]<=char_map[key]:
                count += 1
            # When all characters are found
            if count == n2:
                # Shrink the window
                while (char_map[ord(s[left]) - ord('A')] == 0 or
                    temp_map[ord(s[left]) - ord('A')] > char_map[ord(s[left]) - ord('A')]):
                    if char_map[ord(s[left]) - ord('A')] < temp_map[ord(s[left]) - ord('A')]:
                        temp_map[ord(s[left]) - ord('A')] -=1
                    left += 1
                if right-left+1 < min_window:
                    min_window = right-left+1
                    min_coords = (left, right+1)
        return s[min_coords[0]:min_coords[1]]
    # Time complexity: O(n)
    # Space complexity: O(1)

# s = "OUZODYXAZV"
# t = "XYZ"
# expected = "YXAZ"

# s = "xyz"
# t = "xyz"
# expected = "xyz"
#
# s = "x"
# t = "xy"
# expected= ""

# s="ADOBECODEBANC"
# t="ABC"
# expected="BANC"

# s="aaaaaaaaaaaabbbbbcdd"
# t="abcdd"
# expecetd = "abbbbbcdd"