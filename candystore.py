# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    s=y-x
    if(s>0):
        res=x+s*2
    else:
        res=y
    print(res)