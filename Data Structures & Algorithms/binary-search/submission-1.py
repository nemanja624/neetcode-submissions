class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            m_value = nums[m]

            if m_value == target:
                return m

            elif m_value > target:
                r = m - 1

            else:
                l = m + 1

        return -1   

