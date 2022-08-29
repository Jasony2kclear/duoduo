import math
n, m, a, b  = map(int,input().split())
num1=n//m*b+n%m*a
if a>=b:
    num2=math.ceil(n/m)*b
else:
    num2=n*a
print(min(num1,num2))