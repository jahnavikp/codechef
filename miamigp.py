# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if((107*x)>=(y*100)):
        print("YES")
    else:
        print("NO")