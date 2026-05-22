class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        countW = 0
        ans = 0

        for i in range(k):
            if blocks[i] == 'W':
                countW += 1

        ans = countW

        for right in range(k, len(blocks)):
            left = right - k

            if blocks[right] == 'W':
                countW += 1

            if blocks[left] == 'W':
                countW -= 1

            ans = min(ans, countW)

        return ans