# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i, num in enumerate(nums):
            target_gap = target - num
            if target_gap in elements:
                return sorted([i, elements[target_gap]])
            else:
                elements[num] = i
