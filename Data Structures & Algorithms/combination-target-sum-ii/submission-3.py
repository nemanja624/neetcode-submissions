class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def backtrack(i: int, total: int):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            elif i >= len(candidates) or sum(subset) > target:
                return

            else:
                for j in range(i, len(candidates)):
                    if j > i and candidates[j] == candidates[j - 1]:
                        continue

                    subset.append(candidates[j])
                    backtrack(j + 1, total + candidates[j])
                    subset.pop()

        backtrack(0, 0)

        return res
            

            