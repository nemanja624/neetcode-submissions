class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l <= r:
            m = (l + r) // 2

            curr_sum = 0
            subarray = 1

            for n in nums:
                curr_sum += n

                if curr_sum > m:
                    subarray += 1
                    curr_sum = n

            if subarray <= k:
                r = m - 1
            else:
                l = m + 1

        return l