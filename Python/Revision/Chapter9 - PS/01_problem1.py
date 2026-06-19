f = open("poem.txt")
data = f.read()
if("twinkle" in data):
    print("Twinkle is present in the poem.txt")
else:
    print("Twinkle is not present in the poem.txt")
      
f.close()