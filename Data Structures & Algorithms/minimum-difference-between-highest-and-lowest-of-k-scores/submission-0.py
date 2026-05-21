class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        nums.sort()
        ans = float("inf")

        for left in range(0, len(nums) - k + 1):
            right = left + k - 1
            ans = min(ans, nums[right] - nums[left])

        return ans


