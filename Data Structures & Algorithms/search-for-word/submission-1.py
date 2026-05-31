class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        l = len(word)
        m, n = len(board), len(board[0])
        def helper(i, j, next_target):
            if next_target == l:
                return True
            board[i][j] = '#'
            directions = [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]
            for d in directions:
                adjx, adjy = d[0], d[1]
                if (0<=adjx<m) and (0<=adjy<n) and (board[adjx][adjy]==word[next_target]):
                    if helper(adjx, adjy, next_target+1):
                        board[i][j] = word[next_target-1]
                        return True
            board[i][j] = word[next_target-1] # 当这个递归分支结束后（不管成功还是失败），必须把 board[i][j] 还原，因为其他路径可能合法地经过这个格子
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(i, j, 1):
                        return True
        return False
    