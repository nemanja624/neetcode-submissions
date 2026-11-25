class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        need = total % p

        if need == 0:
            return 0

        current_sum = 0
        seen = {0: -1}

        best = len(nums)

        for i, n in enumerate(nums):
            current_sum += n
            remainder = current_sum % p
            target = (remainder - need) % p

            if target in seen:
                length = i - seen[target]

                if length < best:
                    best = length

            seen[remainder] = i

        if best == len(nums):
            return -1

        return best

    

        

        