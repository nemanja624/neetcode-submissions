class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(index):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            elif sum(subset) > target or index >= len(nums):
                return
            else:
                subset.append(nums[index])
                backtrack(index)
                subset.pop()

                backtrack(index + 1)

        backtrack(0)

        return res
