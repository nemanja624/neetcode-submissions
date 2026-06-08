class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = 0
        countW = 0

        for i in range(k):
            if blocks[i] == "W":
                countW += 1

        ans = countW

        for r in range(k, len(blocks)):
            l = r - k

            if blocks[r] == "W":
                countW += 1

            if blocks[l] == "W":
                countW -= 1
                
            ans = min(ans, countW)

        return ans

        

