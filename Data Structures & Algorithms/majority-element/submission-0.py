from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

            if frequencies[num] >= len(nums) // 2 + 1:
                return num