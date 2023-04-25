import sys; input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
sol = []
visited = [0] * N

def dfs():
    if len(sol) == M:
        print(' '.join(map(str,sol)))
        return
    for i in range(N-1):
        if visited[i] == False:
            sol.append(lst[i])
            visited[i] = True
            dfs()
            visited[i] = False
            sol.pop()
dfs()
