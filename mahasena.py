n=int(input())
a=list(map(int, input().split(" ")))
luck=0
for _ in a:
    if _%2 == 0:
        luck+=1
if (luck>n-luck):
    print("READY FOR BATTLE")
else:
    print("NOT READY")