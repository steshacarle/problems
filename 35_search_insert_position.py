class Solution:
    def searchInsert(self, nums, target):
        # input SORTED array of DISTINCT ints, target value
        # output index of the target or where it would be if in order


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1

        return left

solution = Solution()

print(solution.searchInsert([1, 4, 6, 7], 5))
print(solution.searchInsert([1, 4, 5, 6, 7], 7))
