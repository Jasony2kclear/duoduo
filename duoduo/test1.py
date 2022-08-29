N = int(input())
Q = list(map(int,input().split()))
if N != len(Q) or N>100 or N<1 or max(Q)>1000 or min(Q)<0:
    print("error")
    exit()
print(max(Q)-min(Q))
