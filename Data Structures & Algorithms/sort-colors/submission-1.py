class Solution:
    def sortColors(self, nums: List[int]) -> None:
        white = 0
        red = 0
        blue = 0

        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            else:
                blue += 1

        print(red)
        print(white)
        print(blue)

        for i in range(red):
            nums[i] = 0

        for i in range(red, red + white):
            nums[i] = 1

        for i in range(red + white, len(nums)):
            nums[i] = 2