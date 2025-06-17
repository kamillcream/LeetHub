class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x : (x[1]))
        self.result = 0
        self.end = float('-inf')

        for i in pairs:
            self.connect_chain(i)

        return self.result

    def connect_chain(self, chain):
        if self.end < chain[0]:
            self.end = chain[1]
            self.result +=1
        else:
            return

    