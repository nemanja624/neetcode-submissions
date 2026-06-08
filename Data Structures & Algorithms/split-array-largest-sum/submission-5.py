class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l <= r:
            m = (l + r) // 2
            subarrays = 1
            current_sum = 0

            for n in nums:
                current_sum += n

                if current_sum > m:
                    subarrays += 1
                    current_sum = n

            if subarrays <= k:
                r = m - 1
            else:
                l = m + 1

        return l