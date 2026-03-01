from typing import List
import re

# Time and space complexity for all solutions are O(n)

class Solution:
    # Solution 3 - 100% runtime and 95.35% memory
    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for string in strs:
            encoded_str.append(str(len(string))+"#"+string)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            string = s[j+1:j+1+word_length]
            strs.append(string)
            i = j+word_length+1
        return strs
    # Best solution because the fixed length is being used to parse data

class Solution:
    ## Solution 2 - 100% runtime and 95.35% memory
    import re
    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        concatenated_str = ""
        for i, string in enumerate(strs):
            if i == 0:
                concatenated_str = "_" + str(len(string)) + "#" + string
            else:
                concatenated_str += "_" + str(len(string)) + "#" + string
        return concatenated_str


    def decode(self, s: str) -> List[str]:
        return re.split(pattern=r"_+\d+#", string=s)[1:]
    # Not quite correct as this still runs into delimiter sisks

# Solution 1 - 100% runtime and 95.4% memory
class Solution:
    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        if length == 0:
            return "null"
        concatenated_str = str.join("__", strs)
        return concatenated_str


    def decode(self, s: str) -> List[str]:
        if s == "null":
            return []
        return s.split("__")
# Incorrect because of chances of delimiter collision although it passes the test on neetcode

# message=["Hello","World"]
# message=[""]
#
# encoded_message = encode(message)
# print(encoded_message)
# decoded_message = decode(encoded_message)
# print(decoded_message)

