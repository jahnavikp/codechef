# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    l=0
    res=n*x
    while(res>0):
        l=l+1
        res=res//10
    if(l==5):
        print("YES")
    else:
        print("NO")