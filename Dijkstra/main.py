import heapq  # 우선순위 큐 라이브러리

my_graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 시작 노드부터 현재 배열까지의 거리보다 현재 거리가 크다면 굳이 계산할 필요가 없다.
        if distances[current_node] < current_distance:
            continue

        # 이미 이전 노드랑 연결되어 있는 상태(위를 예로 하면 현재 A-C는 연결되어 있는 상태이고 거리가 1이며 이게 current_distance)
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


print(dijkstra(my_graph, 'A'))
