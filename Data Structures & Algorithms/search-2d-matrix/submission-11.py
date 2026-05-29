class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2
            row = m // COLS
            col = m % COLS
            val = matrix[row][col]

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True

        return False

