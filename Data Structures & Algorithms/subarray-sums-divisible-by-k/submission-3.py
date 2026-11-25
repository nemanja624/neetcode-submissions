class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        seen = {0: 1} 

        for n in nums:
            current_sum += n
            remainder = current_sum % k

            if remainder in seen:
                count += seen[remainder]
                seen[remainder] += 1
            else:
                seen[remainder] = 1

        return count