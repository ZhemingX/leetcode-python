from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ls, res = list(s), []
        def dfs(ls, start):
            if start == len(ls) - 1:
                res.append("".join(ls[:]))
                return
            check = set()
            for i in range(start, len(ls)):
                if ls[i] in check:
                    continue
                check.add(ls[i])
                ls[start], ls[i] = ls[i], ls[start] # swap operation
                dfs(ls, start + 1)
                ls[start], ls[i] = ls[i], ls[start]
        dfs(ls, 0) 
        return res

# T(n) = O(n*n!)
# S(n) = O(n^2)