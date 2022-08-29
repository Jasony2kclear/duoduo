n, m, a, b  = map(int,input().split())
num1=n//m*b+n%m*a
if a>=b:
    num2=round(n/m+0.5)*b
else:
    num2=n*a
print(min(num1,num2))