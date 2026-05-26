class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        found = False

        while l <= r:
            m = (l + r) // 2
            m_val = nums[m]

            if m_val == target:
                found = True
                return m
            elif m_val > target:
                r = m - 1
            else:
                l = m + 1

        if found == False:
            nums.insert(l+1, target)
            return l