class Solution:
    def isValid(self, s: str) -> bool:
        brak = {'{': '}', '[': ']', '(' : ')' }
        openings = []
        for c in s:
            if c in brak:
                openings.append(c)
            elif c in brak.values():
                if not openings or c != brak[openings.pop()]:
                    return False
        return not openings
