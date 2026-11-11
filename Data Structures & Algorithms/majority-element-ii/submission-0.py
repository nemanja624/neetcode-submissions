class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counter = {}

        length = len(nums)
        repetitions = length // 3

        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        for key, value in counter.items():
            if value > repetitions:
                res.append(key)

        return res