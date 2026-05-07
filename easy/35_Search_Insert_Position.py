class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for n in range(len(nums)):
            if nums[n] == target:
                return n
            elif nums[n] > target:
                return n
        if target > nums[len(nums) - 1]:
            return len(nums)
        return -1