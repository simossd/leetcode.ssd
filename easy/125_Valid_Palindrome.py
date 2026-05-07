class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = []
        for c in s:
            if c.isalnum():
                pal.append(c.lower())
        indr = "".join(pal)
        return indr == indr[::-1]