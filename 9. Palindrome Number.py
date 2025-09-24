class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        m = True
        for i in range(math.floor(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                m = False
        return m
