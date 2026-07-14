class Solution(object):
    def isSubsequence(self, s, t):
        start = 0

        for i in range(len(s)):
            for j in range(start, len(t)):
                if s[i] == t[j]:
                    start = j + 1
                    break
            else:
                return False

        return True