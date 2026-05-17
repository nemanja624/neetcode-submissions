class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0

        while left < right:
            top = min(heights[left], heights[right])
            diff = right - left
            if top * diff > maximum:
                maximum = top * diff
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maximum