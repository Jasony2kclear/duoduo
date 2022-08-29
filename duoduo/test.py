import os

L, R = map(int,input().split())
S = input()
print(L,R,S)
if L>R or R>len(S):
    print("Error!")
    exit()
S_1 = S[:L-1]
S_2 = S[L-1:R]
S_3 = S[R:]
print(S_1+S_2[::-1]+S_3)
{:  for  in S_1}
def aan():
    os.write()
