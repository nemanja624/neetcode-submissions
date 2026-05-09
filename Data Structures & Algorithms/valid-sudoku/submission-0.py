class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_set = defaultdict(set)
        row_set = defaultdict(set)
        column_set = defaultdict(set)
    
        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                if value in row_set[i] or value in column_set[j] or value in square_set[(i // 3, j // 3)]:
                    return False

                row_set[i].add(value)
                column_set[j].add(value)
                square_set[(i // 3, j // 3)].add(value)

        return True


