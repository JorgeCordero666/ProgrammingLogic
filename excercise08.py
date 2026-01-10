# Implement a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mult = 1
        for i in nums:
            mult *= i

        if mult > 0:
            return 1
        elif mult < 0:
            return -1
        else:
            return 0
sol = Solution()
nums = [-1,1,-1,1,-1]
print(sol.arraySign(nums))