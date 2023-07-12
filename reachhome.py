# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    res=(x*5)>=y
    if res:
        print("YES")
    else:
        print("NO")