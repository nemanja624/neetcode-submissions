class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        taken_columns = set()
        taken_diagonal1 = set()
        taken_diagonal2 = set()

        def backtrack(row: int):
            if row == n:
                res.append(path.copy())
                return 

            for j in range(n):
                if j not in taken_columns and (row - j) not in taken_diagonal1 and (row + j) not in taken_diagonal2:
                    taken_columns.add(j)
                    taken_diagonal1.add(row - j)
                    taken_diagonal2.add(row + j)
                    path.append("." * j + "Q" + "." * (n - j - 1))
                    backtrack(row + 1)
                    taken_columns.remove(j)
                    taken_diagonal1.remove(row - j)
                    taken_diagonal2.remove(row + j)
                    path.pop()
                else:
                    continue

        backtrack(0)

        return res


            

        

        
        