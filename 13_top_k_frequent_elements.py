from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 3 using bucket sort
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        print(buckets)
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        # Time complexity O(n)
        # Space complexity O(n)

        # # Solution 2
        # freq_map = {}
        # for num in nums:
        #     freq_map[num] = freq_map.get(num, 0) + 1
        # new_list=list(freq_map.items())
        # new_list = sorted(new_list, key=lambda x:x[1], reverse=True)
        # print(new_list)
        # return [x[0] for x in new_list[:k]]
        ## Time complexity O(n log n)
        ## Space complexity O(n)
#
#         # Solution 1 100% memory and 100% runtime but inefficient algorithm
#         freq_map = {}
#         for num in nums:
#             if len(freq_map) == 0:
#                 freq_map[1] = [num]
#             else:
#                 not_found = True
#                 for freq in freq_map.keys():
#                     if num in freq_map[freq]:
#                         freq_map[freq].remove(num)
#                         freq_map[freq + 1] = freq_map.get(freq + 1, []) + [num]
#                         not_found = False
#                         break
#                 if not_found:
#                     freq_map[1] += [num]
#         frequencies = sorted(freq_map.keys(), reverse=True)
#
#         frequent_elements = []
#         i = 0
#         while len(frequent_elements) < k:
#             to_append = freq_map[frequencies[i]]
#             for j,element in enumerate(to_append):
#                 frequent_elements.append(element)
#                 if j>=k:
#                     break
#             i = i+1
#
#         return frequent_elements
#     # Time complexity O(n^2)
#     # Space complexity O(n)
#
# # nums=[4,1,-1,2,-1,2,3]
# # nums=[1,2,2,3,3,3]
# # k=2
