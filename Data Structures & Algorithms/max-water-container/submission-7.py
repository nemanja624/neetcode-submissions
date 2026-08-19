class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maximum = 0

        while l <= r:
            top = min(heights[l], heights[r])
            area = top * (r - l)
            if area > maximum:
                maximum = area

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maximum