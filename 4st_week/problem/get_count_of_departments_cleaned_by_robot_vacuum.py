from collections import deque


current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#   북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
#     a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
#     b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
#     c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
#     d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

def get_d_index_when_rotate_to_left(d) :
    return(d + 3) % 4

def get_d_index_when_go_back(d) :
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    # 2차원 배열 문제가 나오면 무조건 n, m 구하기
    n = len(room_map) # 행(세로)
    m = len(room_map[0]) # 열(가로)
    count_of_departments_cleaned = 1 # 시작 지점은 청소 상태로 시작하기 때문에 1부터 시작

    # BFS
    # 1. 루트 노드를 큐에 넣는다.
    # 2. 현재 큐의 노드를 빼서 visited 에 추가한다.
    # 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
    # 4. 2부터 반복한다.
    # 5. 큐가 비면 탐색을 종료한다.

    # 현재의 위치와 바라보는 방향도 함께 큐에 저장
    queue = deque([[r, c, d]]) #    # 1. 루트 노드를 큐에 넣는다.

    while queue:
        r, c, d = queue.popleft()
        temp_d = d

        for i in range(4) :
            temp_d = get_d_index_when_rotate_to_left(temp_d) # 북 -> 서 -> 남 -> 동
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0 :
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2 #청소한 칸은 2로 표시
                queue.append([new_r, new_c, temp_d])
                break

            # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            elif i == 3: # 반복문을 모두 돌았으면 c 조건에 부합
                temp_d = get_d_index_when_go_back(d) # 바라보는 방향을 유지한 채(처음 상태 = d)
                new_r, new_c =  r + dr[temp_d], c + dc[temp_d]
                queue.append([new_r, new_c, d])

                # d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned

    return


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))