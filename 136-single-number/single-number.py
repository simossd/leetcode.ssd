class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_check = dict.fromkeys(nums)
        for n in nums:
            if n in single_check:
                if single_check[n] is None:
                    single_check[n] = 1
                else:
                    single_check[n] += 1
        for ret, value in single_check.items():
            if value == 1:
                return ret
        return None