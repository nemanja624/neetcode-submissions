class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = dict()
        for i in range(len(nums)):
            key = nums[i]
            if key in my_dict:
                my_dict[key] += 1
            else:
                my_dict[key] = 1
            
            pairs = list(my_dict.items())

        pairs.sort(key = lambda x: x[1], reverse = True)

        top_k_pairs = pairs[0:k]
        res = []

        for num, count in top_k_pairs:
            res.append(num)

        return res



