class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = k - 1

        res = math.inf

        while right < len(nums):
            res = min(res, nums[right] - nums[left])
            right += 1
            left += 1

        return res


