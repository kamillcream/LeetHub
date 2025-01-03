import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.res = []
        self.len = k
        for i in range(len(nums)):
            heapq.heappush(self.res, nums[i])
            if len(self.res) > self.len:
                # 항상 앞에서 pop
                heapq.heappop(self.res)

        

    def add(self, val):
        heapq.heappush(self.res, val)
        if len(self.res) > self.len:
            heapq.heappop(self.res)
        return self.res[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)