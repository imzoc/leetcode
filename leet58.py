class Solution:
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while s[end] == ' ':
            end -= 1
        end += 1
        start = end
        while start >= 1 and s[start - 1] != ' ':
            start -= 1

        return end - start
