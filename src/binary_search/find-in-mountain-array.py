# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # find the peak
        left, right = 0, n-1
        while left <= right:
            middle = (left+right) // 2
            former, latter = mountain_arr.get(middle), mountain_arr.get(middle+1)
            if former < latter:
                left = middle + 1
            elif former > latter:
                right = middle - 1
        maxIndex = left
        
        # search uphill
        left, right = 0, maxIndex
        while left <= right:
            middle = (left+right) // 2
            middleVal = mountain_arr.get(middle)
            if middleVal < target:
                left = middle + 1
            elif middleVal > target:
                right = middle - 1
            else:
                return middle
        
        # search downhill
        left, right = maxIndex, n-1
        while left <= right:
            middle = (left+right) // 2
            middleVal = mountain_arr.get(middle)
            if middleVal > target:
                left = middle + 1
            elif middleVal < target:
                right = middle - 1
            else:
                return middle
        return -1
