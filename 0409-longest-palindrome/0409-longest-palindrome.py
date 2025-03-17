class Solution(object):
    def longestPalindrome(self, s):
        char_cnt = collections.Counter(s)
        length = 0
        odd_found = False

        for count in char_cnt.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
                
        return length + 1 if odd_found else length