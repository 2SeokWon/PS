import sys; input = sys.stdin.readline

N = int(input())
lst = []
visited = [0] * (N+1)
def dfs():
    if len(lst) == N:
        print(' '.join(map(str,lst)))
    for i in range(1,N+1):
        if visited[i] == False:
            lst.append(i)
            visited[i] = True
            dfs()
            visited[i] = False
            lst.pop()

dfs()
        