class Solution:
    def movingCount_dfs(self, m: int, n: int, k: int) -> int:
        def calPoints(m: int) -> int:
            ans = 0
            while m != 0:
                ans += m % 10
                m = m // 10
            return ans

        def dfs(count, i, j):
            # check if (i,j) is valid and could be reached
            if not(0 <= i < m and 0 <= j < n):
                return
            if visited[i][j]:
                return
            if calPoints(i) + calPoints(j) > k:
                return

            visited[i][j] = True
            count[0] += 1

            dfs(count, i+1, j)
            dfs(count, i, j+1)

        count = [0]
        visited = [[False]*n for i in range(m)]
        dfs(count, 0, 0)

        return count[0]

    '''
    dfs 解法中注意点：
     1. visited 套用基本模版数组，其实这里可优化成set，否则空间复杂度固定为 O(MN)
     2. count 用列表表示，是由于 numbers 为不可变类型，传参为传值而不是
     传引用 （当然这个count完全可以采取dfs函数返回结果代替，这里纯属强行count作为全局统计，，）
    '''

    def movingCount_bfs(self, m: int, n: int, k: int) -> int:
        def calPoints(m: int) -> int:
            ans = 0
            while m != 0:
                ans += m % 10
                m = m // 10
            return ans

        from queue import Queue

        visited = set()
        q = Queue()
        q.put((0, 0))

        # while not q.empty():
        #     (x, y) = q.get()
        #     visited.add((x, y))
        #     if 0 <= (x+1) < m and 0 <= y < n and (x+1, y) not in visited and calPoints(x+1) + calPoints(y) <= k:
        #         q.put((x+1, y))
        #     if 0 <= x < m and 0 <= (y+1) < n and (x, y+1) not in visited and calPoints(x) + calPoints(y+1) <= k:
        #         q.put((x, y+1))

        while not q.empty():
            (x, y) = q.get()
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and calPoints(x) + calPoints(y) <= k:
                visited.add((x, y))
                q.put((x+1, y))
                q.put((x, y+1))

        return len(visited)

    '''
    bfs中注意点：
    核心块的while代码有两种implement（注释和非注释的），肉眼看具有相同的语义，但注释块会出现代码超时（比如执行下面的数据），目前不知道原因在哪儿
    '''


# s = Solution()
# print(s.movingCount_bfs(30, 10, 15))
