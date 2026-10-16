class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i: int):
            if sum(path) == target:
                res.append(path.copy())
                return

            elif sum(path) > target or i >= len(nums):
                return

            else:
                path.append(nums[i])
                backtrack(i)
                path.pop()

                backtrack(i + 1)

        backtrack(0)

        return res

            