import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        heap = []
        res = []
        
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        while heap:
            freq, char = heapq.heappop(heap)
            
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    break  
                
                next_freq, next_char = heapq.heappop(heap)
                res.append(next_char)
                
                if next_freq + 1 < 0:
                    heapq.heappush(heap, (next_freq + 1, next_char))
                
                heapq.heappush(heap, (freq, char))
            else:
                res.append(char)
                if freq + 1 < 0:
                    heapq.heappush(heap, (freq + 1, char))
        
        return ''.join(res)
