from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(dict.fromkeys(nums))
        return len(nums)  


test = Solution()
print(test.removeDuplicates([1,1,2]))