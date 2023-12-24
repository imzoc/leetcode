from icecream import ic

class Solution:
    def maximumStrongPairXor(self, nums: list) -> int:
        l = []
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    l.append((x, y))
        max_xor = 0
        for x, y in l:
            max_xor = max(max_xor, x ^ y)
        return max_xor

'''
solution = Solution()
ic(7 == solution.maximumStrongPairXor([1,2,3,4,5]))
ic(0 == solution.maximumStrongPairXor([10, 100]))
ic(7 == solution.maximumStrongPairXor([5,6,25,30]))
'''