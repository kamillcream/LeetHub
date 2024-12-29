class Solution(object):
    def leastInterval(self, tasks, n):
        counter = collections.Counter(tasks)
        res = 0

        while True:
            sub_cnt = 0

            for task, _ in counter.most_common(n+1):
                sub_cnt += 1
                res += 1
                counter.subtract(task)

                counter += collections.Counter()

            if not counter:
                break

            res += n - sub_cnt + 1
        
        return res
        
        