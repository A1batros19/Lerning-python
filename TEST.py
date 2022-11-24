a1 = input()
b1 = input()
c1 = input()
a = len(a1)
b = len(b1)
c = len(c1)
min1=min(a,b,c)
max1=max(a,b,c)
mid1=(a+b+c)-(min1+max1)
if mid1-min1==max1-mid1:
    print('YES')
else:
    print('NO')

