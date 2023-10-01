N=int(input())
k=[]
for i in range(N):
    name = input()
    score = float(input())
    k.append([name,score])
print(k)
m=min(k)
print(m)