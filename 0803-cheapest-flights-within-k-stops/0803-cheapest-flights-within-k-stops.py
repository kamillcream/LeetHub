import heapq
import collections

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # 그래프 생성
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 우선순위 큐 초기화
        q = [(0, src, K + 1)]  # (비용, 현재 노드, 남은 중간 경유지 수)
        visited = {}  # (노드, 남은 k): 최소 비용 저장
        
        while q:
            price, node, k = heapq.heappop(q)
            
            # 목적지에 도달하면 비용 반환
            if node == dst:
                return price
            
            # 중간 경유지 횟수가 남아있는 경우
            if k > 0:
                for neighbor, weight in graph[node]:
                    new_cost = price + weight
                    # 방문하지 않았거나 더 적은 비용으로 도달한 경우에만 진행
                    if (neighbor, k - 1) not in visited or visited[(neighbor, k - 1)] > new_cost:
                        visited[(neighbor, k - 1)] = new_cost
                        heapq.heappush(q, (new_cost, neighbor, k - 1))
        
        return -1  # 경로를 찾을 수 없는 경우
