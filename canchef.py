# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    f=x*15
    if(f>=y*2):
        print("YES")
    else:
        print("NO")