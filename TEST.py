m=int(input())
n=int(input())
if m<n:
    for i in range(n, m-1,-1):
        print(i)
else:
    for i in range(n, m):
        print(i)

