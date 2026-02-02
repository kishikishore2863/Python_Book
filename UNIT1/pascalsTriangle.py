from typing import List
class S:
    def pas(self,n:int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        prev = self.pas(n-1)
        new = [1]*n

        for i in range(1,n-1):
            new[i] = prev[-1][i-1]+prev[-1][i]

        prev.append(new)

        return prev



s=S()
print(s.pas((10)))