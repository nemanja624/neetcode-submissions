class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == '.':
                    continue

                if value in rows[i] or value in cols[j] or value in sqrs[(i//3, j//3)]:
                    return False

                rows[i].add(value)
                cols[j].add(value)
                sqrs[(i//3, j//3)].add(value)

        return True

                