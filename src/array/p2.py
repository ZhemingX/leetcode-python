from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False

        sr, sc = 0, len(matrix[0]) - 1

        while(sr < len(matrix) and sc >= 0):
            if matrix[sr][sc] == target:
                return True
            if matrix[sr][sc] > target:
                sc -= 1
            else:
                sr += 1

        return False

# T: O(m+n)
