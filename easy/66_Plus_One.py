class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_placed = []
        digits = digits[::-1]
        if digits[0] == 9 and len(digits) == 1:
            return [1, 0]
        for i in range(len(digits)):
            if i == 0 and digits[i] == 9:
                digits[0] = 10
                digits[1] = digits[1] + 1
                new_placed.append(0)
            elif i == 0 and digits[i] != 10 and digits[i] != 9:
                new_placed.append(digits[0] + 1)
            elif digits[i] == 10:
                if i + 1 < len(digits):
                    digits[i + 1] = digits[i + 1] + 1
                    new_placed.append(0)
                else:
                    new_placed.append(0)
                    new_placed.append(1)
            else:
                new_placed.append(digits[i])
        return new_placed[::-1]
