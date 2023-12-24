class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        pd_hash = [[u == e for u in range(len(s))] for e in range(len(s))]
        print(pd_hash)

        for end in range(len(s)):
            for start in range(end, -1, -1):
                pd_hash[start][end] = (s[start] == s[end]) and (end - start < 2 or pd_hash[start+1][end -1])
#                print(s[start:end+1] + "\t" + str(start) + " " + str(end) + '\t' + str(start - end + 1))
                if pd_hash[start][end] and end - start + 1 > len(longest):
                    longest = s[start:end + 1]

        for u in range(len(s)):
            print(pd_hash[u])
        return longest


print(Solution.longestPalindrome(None, "babad"))