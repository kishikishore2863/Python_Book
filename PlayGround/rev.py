class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x>0:
            last = x%10
            rev = rev*10+last
            x=x//10
        return rev

s = Solution()
res = s.reverse(123)
print(res)