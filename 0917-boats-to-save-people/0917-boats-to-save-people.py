class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        res = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            res += 1
        return res