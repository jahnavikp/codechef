# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n-m<=0:
        print (n)
    else:
        print((2*n)-m)