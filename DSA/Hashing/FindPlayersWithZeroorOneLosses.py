from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        winnersList = []
        for l in matches:
            winners[l[0]] = 0

        for l in matches:
            if l[1] in winners:
                del winners[l[1]]

        for k in winners.keys():
            winnersList.append(k)

        lastOne = []
        last = {}
        for l in matches:
            if l[1] in last:
                last[l[1]] += 1
            else:
                last[l[1]] = 1
        for k, v in last.items():
            if v == 1:
                lastOne.append(k)
                print(lastOne)
        winnersList.sort()
        lastOne.sort()
        return [winnersList,lastOne]



s =Solution()
res =  s.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
print(res)