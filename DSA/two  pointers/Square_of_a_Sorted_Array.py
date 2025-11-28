from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list = [0] * len(nums)
        start = 0
        end = len(nums) - 1
        i = len(nums) - 1
        while start <= end:
            if abs(nums[start]) >= abs(nums[end]):
                list[i] = nums[start] ** 2
                start = start + 1
            else:
                list[i] = nums[end] ** 2
                end = end - 1
            i = i - 1
        return list        

