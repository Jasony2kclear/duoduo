N = input()
for i in range(3):
    Cnt = 0
    for j in range(3):
        if N[i]==N[j]:
            Cnt+=1
    if Cnt == 1 :
        print(N[i])
        exit(0)
print("-1")
