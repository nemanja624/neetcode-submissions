class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        res = 0

        for n in nums:
            if n == 1:
                current += 1

            res = max(res, current)

            if n == 0:
                current = 0

        return res