s = input()
k = int(input())
found = False

for i in range(len(s)):
    ch = s[i]
    t = ''
    for j in range(k):
        if (i+j) >= len(s):
            break
        #print(f't = {t}, s[i+j] = {s[i+j]}')
        if s[i+j] in t:
            break
        t = t + s[i+j]
        #print(f't = {t} (must have added {s[i+j]})')
    if len(t) == k:
        found = True
        break
        

if found:
    answer = "Yes"
else:
    answer = "No"
print(answer)
#aabbccddeeff