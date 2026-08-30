s = input()
p = input()
count = 0

i = 0
k = len(p)
while(i+k <= len(s)):
    if(s[i:i+k] == p):
        count+=1
    i+=1

print(count)