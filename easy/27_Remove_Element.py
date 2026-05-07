class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        elements = []
        for n in nums:
            if n != val:
                elements.append(n)
        nums[:] = elements
        return len(nums)