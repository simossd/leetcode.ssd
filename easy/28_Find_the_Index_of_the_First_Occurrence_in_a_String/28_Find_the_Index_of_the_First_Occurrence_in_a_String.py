class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                k = 0
                now = i
                while k < len(needle) and i < len(haystack) and haystack[i] == needle[k]:
                    i+=1
                    k+=1
                if k == len(needle):
                    return now
        return -1


test = Solution()
print(test.strStr("leetcode", "leeto"))