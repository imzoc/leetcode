class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        middle = len(nums) // 2
        if nums[middle] == target: 
            return middle
        elif nums[middle] < target:
            if middle == 0:
                return 1
            return middle + self.searchInsert(nums[middle:], target)
        else:
            if middle == 0:
                return 0
            return self.searchInsert(nums[:middle], target)

