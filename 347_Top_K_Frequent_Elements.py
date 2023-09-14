# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        nums_count = {}
        for num in nums:
            if num in nums_count.keys():
                nums_count[num] = nums_count[num] + 1
            else:
                nums_count[num] = 1

        for i in range(0, k):
            t = max(nums_count, key=nums_count.get)
            result.append(t)
            del nums_count[t]
        return result
    