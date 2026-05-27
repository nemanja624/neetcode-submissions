class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = min(nums)
        r = max(nums)

        return l