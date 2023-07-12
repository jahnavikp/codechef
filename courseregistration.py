# cook your dish here
t=int(input())
for i in range(t):
    m,k,n=map(int,input().split())
    if((k-n)>=m):
        print("Yes")
    else:
        print("No")