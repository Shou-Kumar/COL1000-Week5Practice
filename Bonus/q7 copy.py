s = input()
w = int(input())
count = 0
length = 0

for i in range(len(s)):
    for j in range(len(s) - i ):
        st = s[i:i+j+1]
        wt = 0
        for k in st:
            wt += ord(k) - ord('a') + 1
        if wt == w: 
            if(len(st) > length):
                length = len(st)
# Write your program here.
# The alphabetic value of my char is:
# ord(my char) - ord('a') + 1
print(length)