from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)  # O(1) 탐색 위해 set 사용
        if endWord not in wordSet:
            return 0

        q = deque()
        q.append((beginWord, 1))  # (현재 단어, 단계 수)

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)  # 방문 처리
                        q.append((newWord, steps + 1))

        return 0