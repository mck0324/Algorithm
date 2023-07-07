import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    result = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = -1
            result += dfs(nx,ny)
    return result

n = int(input())
graph = [[0] * n for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(n):
        graph[i][j] = int(row[j])

anwser = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = -1
            anwser.append(dfs(i,j))
anwser.sort()
print(len(anwser))
for i in range(len(anwser)):
    print(anwser[i])