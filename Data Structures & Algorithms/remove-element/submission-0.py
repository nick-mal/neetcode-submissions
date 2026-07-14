class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_removed = 0

        for ind in range(len(nums)):
            if nums[ind - num_removed] == val:
                del nums[ind - num_removed]
                num_removed += 1

        return len(nums)