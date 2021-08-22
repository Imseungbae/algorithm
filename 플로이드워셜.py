#플로이드 워셜 알고리즘 구현
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
INF = int(1e9)

# distance 2차원배열
distance = [ [INF]*(v+1) for i in range(v+1) ]

for i in range(e):
    a,b,c = map(int, input().split())
    print(a)
    distance[a][b] = c
# i==j인경우 0으로 셋팅
for i in range(len(distance)):
    for j in range(len(distance[i])):
        if i == j :
            distance[i][j] = 0

def printDist():
    for i in range(1, len(distance)):
        print( distance[i][1:] )

def warshall():
    for i in range(1, v+1):
        for j in range(1, v+1):
            for k in range(1, v+1):
                    distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])


warshall()
printDist()