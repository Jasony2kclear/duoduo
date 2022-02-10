t = int(input())
ans=['']
for i in range(t):
    s=input()
    if len(s) % 2 > 0:
        ans.append("NO")
    else:
        print(s[:-(len(s) // 2)])
        print(s[(len(s) // 2) - 1:])
        if s[-(len(s) // 2)] == s[(len(s) // 2) - 1]:
            ans.append("YES")
        else:
            ans.append("NO")
print(ans)