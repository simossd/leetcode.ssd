class Solution:
    def reverse(self, x: int) -> int:
        if 2147483647 < x < -2147483648:
            return 0
        x = str(x)
        x = list(x)
        if x[0] == '-':
            x.pop(0)
            num = int("".join(x)[::-1]) * -1
        else:
            num = int("".join(x)[::-1])
        if 2147483647 < num or num < (-2147483648):
            return 0
        return num