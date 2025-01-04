import collections

class Solution(object):
    def topKFrequent(self, words, k):
        # Count the frequency of each word
        counter = collections.Counter(words)
        
        # Sort the words first by frequency (descending), then by word (alphabetically)
        sorted_words = sorted(counter.keys(), key=lambda x: (-counter[x], x))
        
        # Return the top k frequent words
        return sorted_words[:k]
