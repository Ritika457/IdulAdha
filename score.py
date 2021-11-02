
n = int(input())
scores = list(map(int,input().split()))
x=set(scores)
a=max(x)
x.remove(a)
b=max(x)
print(b)

