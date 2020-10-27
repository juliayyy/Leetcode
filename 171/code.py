class Solution:
    def titleToNumber(self, s: str) -> int:
        s1 = list(s)
        s1.reverse()
        s2 = list(enumerate(s1))
        res = 0
        for i, ch in s2:
            res = res + 26**i*(ord(ch)-64)
        return res