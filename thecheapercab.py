# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(x>y):
        print("SECOND")
    elif(x==y):
        print("ANY")
    else:
        print("FIRST")