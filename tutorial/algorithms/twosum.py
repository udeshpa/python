
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    nums.sort(reverse=False)
    n = len(nums)

    if n < 2:
      return []

    for i in range(0, n-1):

      if nums[i] > target:
        break


      for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
          ret = [i, j]
          return ret


sol = Solution()

nums = [2,7,11,15]
target = 9


ret = sol.twoSum(nums, target)

print(ret)

nums = [3,2,4]
target = 6

ret = sol.twoSum(nums, target)

print(ret)

nums = [3,3]
target = 6

ret = sol.twoSum(nums, target)
print(ret)
