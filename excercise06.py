# Given an array nums, move all 0's to the end of it while maintaining the relative order of
# the non-zero elements

# Note that you must do this in-place without making a copy of the array.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
            else:
                continue
        return nums

sol = Solution()
array = [0,0,1]
print(sol.moveZeroes(array))


