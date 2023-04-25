import sys; input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
sol = []

def dfs():
    if len(sol) == M:
        print(' '.join(map(str,sol)))
        return
    for i in range(N):
        sol.append(lst[i])
        dfs()
        sol.pop()

dfs()
