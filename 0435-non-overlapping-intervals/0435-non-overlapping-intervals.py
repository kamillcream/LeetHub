class Solution(object):
    def eraseOverlapIntervals(self, intervals):

        self.start, self.end = float('inf'), float('-inf')
        eliminated = 0

        intervals.sort(key = lambda x: x[1])
        
        for i in intervals:
            if self.in_range(i[0], i[1]):
                eliminated += 1
            else: self.reset_two_pointers(i[0], i[1])

        return eliminated

    def reset_two_pointers(self, s, e):
        if self.start > s:
            self.start = s
        if self.end < e:
            self.end = e

    def in_range(self, s, e):
        return s < self.end and e > self.start

        