from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 1
        e = len(nums)-1
        p = 0
        k = 0
        while s <= e:
            if nums[p] != nums[s]:
                k += 1
                p += 1
                temp = nums[s]
                nums[p] = nums[s]
                # nums[e] = temp
                # e -= 1
            s += 1
        return k

s = Solution()
l = [0,0,1,1,1,2,2,3,3,4]
res = s.removeDuplicates(l)
print(res)


