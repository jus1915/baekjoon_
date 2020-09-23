N,M,B=[*map(int,input().split())]
land = [[*map(int,input().split())] for i in range(N)]
m,M=min(min(land)),max(max(land))
L = []
for k in range(m,M+1):
    sum = 0
    n = 0
    for i in range(N):
        for j in range(M):
            if land[i][j]>=k:
                sum+=2*(land[i][j]-k)
            else:
                sum+=(k-land[i][j])
                n+=k-land[i][j]