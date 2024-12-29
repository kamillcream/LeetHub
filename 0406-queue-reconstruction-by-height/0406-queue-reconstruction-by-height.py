class Solution(object):
    def reconstructQueue(self, people):
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        res = []

        while heap:
            person = heapq.heappop(heap)
            res.insert(person[1], [-person[0], person[1]])

        return res
        
        