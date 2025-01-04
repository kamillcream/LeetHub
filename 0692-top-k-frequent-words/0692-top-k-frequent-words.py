import collections

class Solution(object):
    def topKFrequent(self, words, k):
        counter = collections.Counter(words)
        
        sorted_words = sorted(counter.keys(), key=lambda x: (-counter[x], x))
        
        return sorted_words[:k]
