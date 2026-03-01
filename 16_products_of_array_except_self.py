from typing import List

class Solution:
    # Solution 1 - 100% Runtime and 100% Memory
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        prefix_product, suffix_product = 1, 1
        for i in range(length):
            products[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(length - 1, -1, -1):
            products[i] *= suffix_product
            suffix_product *= nums[i]
            print(products)
        return products
    # Time complexity: O(n)
    # Space complexity: O(n)

# nums = [1,2,4,6]
# expected = [48,24,12,8]
#
# print(productExceptSelf(nums))
