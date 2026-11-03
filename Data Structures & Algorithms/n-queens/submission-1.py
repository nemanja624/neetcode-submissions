class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []

        taken_col = set()
        taken_diag1 = set()
        taken_diag2 = set()

        def backtrack(row: int):
            if row == n:
                res.append(path.copy())
                return

            for j in range(n):
                if j in taken_col or (row - j) in taken_diag1 or (row + j) in taken_diag2:
                    continue
                else:
                    taken_col.add(j)
                    taken_diag1.add(row - j)
                    taken_diag2.add(row + j)
                    path.append("." * j + "Q" + "." * (n - j - 1))
                    backtrack(row + 1)
                    taken_col.remove(j)
                    taken_diag1.remove(row - j)
                    taken_diag2.remove(row + j)
                    path.pop()

        backtrack(0)

        return res

            

        

        
        