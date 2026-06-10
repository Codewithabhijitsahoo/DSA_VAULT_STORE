# Title: Two Sum
# Difficulty: EASY
# Platform: LeetCode
# Link: https://leetcode.com/problems/two-sum/
#

class Solution:
      def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
          if target - num in seen:
            return [seen[target - num], i]
          seen[num] = i
        return []
        # updated comment
        #update