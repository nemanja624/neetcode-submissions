class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        l = 0
        results = []

        for r in range(len(nums)):
            while deq and nums[r] > deq[-1]:
                deq.pop()

            deq.append(nums[r])

            if (r - l + 1) == k:
                results.append(deq[0])
                l += 1
                if nums[l-1] == deq[0]:
                    deq.popleft()

        return results