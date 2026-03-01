from typing import List
from collections import Counter

# 100
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        char_count = Counter()
        # Contiguous substrings required
        # Record the frequency of each element in the window
        for right in range(len(s)):
            char_count[s[right]] += 1
            max_freq = max(max_freq, char_count[s[right]])  # non-repeating characters in the window should not be greater than k
            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left+=1
        print(char_count, left, right, max_freq)
        return len(s)-left
    # Time complexity: O(n)
    # Space complexity: O(m) m for unique elements

# s = "XYYX"
# k = 2
# expected = 4

# s = "AAABABB"
# k = 1
# expected = 5

# s = "AABABBAABABA"
# k = 2
# expected = 6