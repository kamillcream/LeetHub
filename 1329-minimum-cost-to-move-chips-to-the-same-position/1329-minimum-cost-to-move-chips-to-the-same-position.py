class Solution(object):
    def minCostToMoveChips(self, position):
        cnt_odd = sum(1 for p in position if p % 2 == 0)
        cnt_even = len(position) - cnt_odd

        return min(cnt_odd, cnt_even)        