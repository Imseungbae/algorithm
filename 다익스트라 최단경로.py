import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 나타내는 10억(1,000,000,000)으로 설정

#노드와 간선 갯수 입력받기
v,e = map(int, input().split())
graph = [[] for i in range(v+1)]
#방문체크리스트 만들기
visit = [0] * (v+1)
#최단경로 테이블
distance = [INF] * (v+1)

start = int(input())

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


            

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 #가장최단거리가 짧은노드
    for i in range(1, v+1):
        if distance[i] < min_value and visit[i] is not 1:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    # 방문처리
    visit[start] = 1
    # 현재 출발점을 기준으로 최단테이블 갱신
    for j in graph[start]:
        distance[ j[0] ] = j[1]

    # 시작노드를 제외한 전체(v-1)개의 노드에 대해 반복
    for _ in range(v-1):
        now = get_smallest_node()
        visit[now] = 1
        print("now", now)
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, v+1):
    print(distance[i])