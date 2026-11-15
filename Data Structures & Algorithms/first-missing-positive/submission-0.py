class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        seen = {}

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        while res in seen:
            res += 1

        return res
