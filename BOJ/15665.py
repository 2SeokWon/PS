import sys ; input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
sol = []
pre = 0

def dfs():
    pre = 0
    if len(sol) == M:
        print(' '.join(map(str,sol)))
        return

    for i in range(N):
        if pre != lst[i]:
            sol.append(lst[i])
            pre = lst[i]
            dfs()       
            sol.pop()
        
dfs()