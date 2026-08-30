s = input()
L = int(input())
R = int(input())
mismatch = False

t = R
for i in range(L,R+1):

    if(s[i] != s[t]):
        mismatch = True
    t-=1
    if i>=t:
        break

if mismatch:
    answer = "No"
else:
    answer = "Yes"
print(answer)