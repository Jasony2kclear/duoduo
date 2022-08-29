k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if k < 1 or k > 10:
    print("1>=k<=10 ERROR!")
    exit()

if l < 1 or l > 10:
    print("1>=l<=10 ERROR!")
    exit()

if m < 1 or m > 10:
    print("1>=m<=10 ERROR!")
    exit()

if n < 1 or n > 10:
    print("1>=n<=10 ERROR!")
    exit()

if d < 1 or d > 100000:
    print("1>=m<=10 ERROR!")
    exit()

result = []
for i in range(d // k):
    if i * k not in result:
        result.append(i * k)
for i in range(d // l):
    if i * l not in result:
        result.append(i * l)
for i in range(d // m):
    if i * m not in result:
        result.append(i * m)
for i in range(d // n):
    if i * n not in result:
        result.append(i * n)
print(len(result))
