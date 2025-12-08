from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        res = []
        for i in range(len(nums)):
            if target-nums[i] in map1:
                res.append(map1[target-nums[i]])
                res.append(i)
                return res
            else:
                map1[nums[i]]=i

        return res


# s = Solution()
# l2 = [2,7,11,15]
# print(s.twoSum(l2,9))
arr = [0]*26
print(ord('a'))