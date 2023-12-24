import leet35


s = leet35.Solution()

assert s.searchInsert([1,3,5,6], 5) == 2
assert s.searchInsert([1,3,5,6], 2) == 1

assert s.searchInsert([1,3,5,7], 6) == 3
assert s.searchInsert([1,3,5,6], 7) == 4
