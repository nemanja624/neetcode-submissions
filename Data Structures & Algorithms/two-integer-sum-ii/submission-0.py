class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(numbers) - 1

        while left < right: 
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] == target:
                res.append(left+1)
                res.append(right+1)
                break
            else:
                return False

        return res
