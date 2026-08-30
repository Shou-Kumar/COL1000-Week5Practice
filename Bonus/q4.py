s = input()
result = ""
count = 0

i = 0
while i < len(s):

    if i < len(s) - 1 and s[i] == s[i+1]:
            result = result + "*"
            count+=1
            i+=2
    else:
        result = result + s[i]
        i+=1

print(result)
print(count)