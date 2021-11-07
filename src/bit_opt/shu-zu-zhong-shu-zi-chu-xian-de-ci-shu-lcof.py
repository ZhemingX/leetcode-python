from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res, cn, a, b = 0, 1, 0, 0
        for n in nums:
            res ^= n
        #xor_res = reduce(lambda x, y: x ^ y, nums)
        while not res & cn: cn <<= 1
        for n in nums:
            if n & cn: a ^= n
            else: b ^= n
        return a, b