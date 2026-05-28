class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [-1, -1]

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                res[0] = m

            if nums[m] >= target:
                r = m -1
            else:
                l = m + 1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                res[1] = m
            
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1

        return res