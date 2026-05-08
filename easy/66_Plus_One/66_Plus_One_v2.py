class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        somme = 0
        for n in digits:
            somme = (somme * 10) + n
        somme += 1
        result = []
        while somme > 0:
            r = somme % 10
            somme //= 10
            result.append(r)
        return result[::-1]