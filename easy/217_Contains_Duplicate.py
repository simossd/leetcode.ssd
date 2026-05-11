class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_d = dict.fromkeys(nums)
        return not len(nums) == len(nums_d)