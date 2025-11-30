class Solution(object):
    def buildArray(self, target, n):
        answer = []
        stack = []

        for i in range(1, n + 1):
            stack.append(i)
            answer.append("Push")

            if stack == target:
                break

            if i not in target:
                stack.remove(i)
                answer.append("Pop")

        return answer
        