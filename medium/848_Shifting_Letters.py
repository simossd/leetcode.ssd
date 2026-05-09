class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifted = []
        alphas = list(s)[::-1]
        sum = 0
        for n in alphas:
            sum += shifts.pop()
            shifted.append(chr((ord(n) - ord('a') + sum) % 26 + ord('a')))
        return "".join(shifted[::-1])
