class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        max_freq = 0
        total = 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > k + total:
                total -= nums[l]
                l += 1

            max_freq = max(max_freq, r - l + 1)

            r += 1

        return max_freq

    
        


