import collections as c

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = c.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())
        