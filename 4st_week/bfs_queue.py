from collections import deque

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 1. 루트 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited 에 추가한다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
# 4. 2부터 반복한다.
# 5. 큐가 비면 탐색을 종료한다.

def bfs_queue(adj_graph, start_node):
    queue = deque([start_node])
    visited = [start_node]

    while queue :
        current_node = queue.popleft() # 1 -> 2
        for adjacent_node in adj_graph[current_node]: # 2, 3, 4
            if adjacent_node not in visited:
                queue.append(adjacent_node) # 2, 3, 4
                visited.append(adjacent_node) # visited = 1

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!