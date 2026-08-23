class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()

        for n in nums:
            if n in my_set:
                return n
            else:
                my_set.add(n)