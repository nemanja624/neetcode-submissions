class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        path = set()

        def backtrack(i: int, j: int, k: int):
            if k == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[k] or (i, j) in path:
                return False

            path.add((i, j))

            res = backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1) or backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1)

            path.remove((i, j))

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    boolean = backtrack(i, j, 0)
                    if boolean == True:
                        return True

        return False




        
            