f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present in Poem.txt file")
else:
    print("Twinkle is not present in Poem.txt file")
f.close()