s = "Dr Abdul Kalaam Visionary Leader"
word = s.split()
longest = ""
for i in word:
    if len(i) > len(longest):
        longest = i
print(longest)