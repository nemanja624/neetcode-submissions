class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        max_count = 0

        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        for key, value in counter.items():
            if value > max_count:
                max_count = value
                res = key

        return res

        