s = input()
vowels = 0
consonants = 0

v = 'aeiou'
c = 'qwrtypsdfghjklzxcvbnm'
for i in s:
    if i in v:
        vowels+=1
    elif i in c:
        consonants+=1


if vowels == consonants:
    answer = "Balanced"
else:
    answer = "Not Balanced"
print(answer)