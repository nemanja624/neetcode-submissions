class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pairs:
                return [pairs[diff], i]
            else:
                pairs[nums[i]] = i