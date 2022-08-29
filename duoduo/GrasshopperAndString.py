a=str(input()).upper()
if len(a)>100:
    print("String length should less 100 characters!")
    exit()
vowel=['A','E','I','O','U','Y']
result=[]
i=0
j=0
for i in range(len(a)):
    j+=1
    if a[i] in vowel:
        result.append(j)
        j=0
result.append(j+1)
print(result)
print(max(result))