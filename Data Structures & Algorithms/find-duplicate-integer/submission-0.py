class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        current = nums[0]
        hashmap = {}

        for n in nums:
            if n in hashmap:
                return n
            else:
                hashmap[n] = 1

        


        