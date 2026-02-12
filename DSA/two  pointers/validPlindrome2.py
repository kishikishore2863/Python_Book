class Solution:
    def validPalindrome(self, s: str) -> bool:
        start =0
        end =len(s)-1
        count =0
        while start<end:
            if s[start] != s[end]:
                return self.isPlaindrome(start+1,end,s) or self.isPlaindrome(start,end-1,s)
            start +=1
            end -=1
        return True

    def isPlaindrome(self,start,end,s):
        while start<end:
            if s[start]!=s[end]:
                return False
            start +=1
            end -=1
        return True