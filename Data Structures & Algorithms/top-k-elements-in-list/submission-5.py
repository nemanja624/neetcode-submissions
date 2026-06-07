class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        for key, value in count.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


