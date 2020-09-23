L=[]
K = int(input())
for i in range(K):
    N=int(input())
    if N == 0:
        L.pop(len(L)-1)
    else:
        L.append(N)
print(sum(L))