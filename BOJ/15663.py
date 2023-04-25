import sys ; input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
sol = []
visited = [0] * N
pre = 0

def dfs():
    pre = 0
    if len(sol) == M:
        print(' '.join(map(str,sol)))
        return

    for i in range(N):
        if pre != lst[i] and visited[i] == False:
            sol.append(lst[i])
            pre = lst[i]
            visited[i] = True
            dfs()
            visited[i] = False
            sol.pop()
        
dfs()