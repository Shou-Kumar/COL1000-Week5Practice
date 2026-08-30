a = input()
b = input()
k = int(input())
answer = "None"

i = 0
while(i+k <= len(a)):
    a0 = ''
    for j in a[i:i+k]:
        a0 = a0 + j
    if a0 in b:
        answer = a0
        break
    i+=1

    
print(answer)