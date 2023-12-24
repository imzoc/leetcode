class Solution:
    def minOperations(self, s1: list, s2: list) -> int:
        c, ci = 0, 0
        for u in range(len(s1)):
            if (s1[u] > s1[-1] and s2[u] > s1[-1])\
            or (s1[u] > s2[-1] and s2[u] > s2[-1])\
            or (s1[u] > s1[-1] and s1[u] > s2[-1])\
            or (s2[u] > s2[-1] and s2[u] > s1[-1]): 
                return -1       # impossible -- this holds for inverted last index lists as well
            if s1[u] > s1[-1] or s2[u] > s2[-1]:
                c += 1
            if s1[u] > s2[-1] or s2[u] > s1[-1]:
                ci += 1
        return min(c, ci)


from icecream import ic
solution = Solution()
ic(solution.minOperations([1,2,7], [4,5,3]))
ic(solution.minOperations([2,3,4,5,9], [8,8,4,4,4]))
ic(solution.minOperations([1,5,4], [2,5,3]))
ic(solution.minOperations([17,13,19,9,6,14],[17,14,15,1,19,19]))
ic(solution.minOperations([10,18,12,12],[19,6,5,12]))