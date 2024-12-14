from collections import deque

class Solution(object):
    def isPalindrome(self, s):
        strs = deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

        