from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(visited: List[List[bool]], i, j, w_index) -> bool:
            # list range check
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or w_index >= len(word):
                return False
            # condition check
            if visited[i][j] or board[i][j] != word[w_index]:
                return False

            visited[i][j] = True
            if len(word) - 1 == w_index:
                return True
            res = dfs(visited, i+1, j, w_index + 1) or dfs(visited, i-1, j, w_index +
                                                           1) or dfs(visited, i, j+1, w_index + 1) or dfs(visited, i, j-1, w_index + 1)
            visited[i][j] = False
            return res

        visited = [[False]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(dfs(visited, i, j, 0)):
                    return True
        return False

# T: O(MN*3^k) (word length k, M*N board)
