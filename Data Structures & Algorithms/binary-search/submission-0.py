class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = begin + (end - begin) // 2
            mid_value = nums[mid]
            if mid_value == target:
                return mid

            elif target < mid_value:
                end = mid - 1

            else:
                begin = mid + 1

        return -1

