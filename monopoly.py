# cook your dish here
t=int(input())
for i in range(t):
    p,q,r,s =map(int,input().split())
    if(p>(q+r+s)):
        print("YES")
    elif(q>(p+r+s)):
        print("YES")
    elif(r>(p+q+s)):
        print("YES")
    elif(s>(p+q+r)):
        print("YES")
    else:
        print("NO")
