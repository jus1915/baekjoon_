L=int(input())
list=[*map(int,input().split(' '))]
N = int(input())
for i in range(N):
    s,k = map(int,input().split(' '))
    if s==1:
        for i in range(k-1, L, k):
            list[i] = 1 - list[i]
    elif s==2:
        for i in range(min(k-1,L-k)+1):
            if list[k-1-i]!=list[k-1+i]:
                break
            else:
                list[k-1-i]=list[k-1+i]=1-list[k-1-i]

R = [list[i:min(i+20, L)] for i in range(0, L, 20)]
print(R)
for x in R:
    print(' '.join(map(str, x)))