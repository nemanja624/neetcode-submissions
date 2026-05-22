class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = k - 1
        res = math.inf

        for i in range(k):
            res = nums[right] - nums[left]

        for right in range(k, len(nums)):
            left += 1

            curr_diff = nums[right] - nums[left]
            if curr_diff < res:
                res = curr_diff

        return res
            


