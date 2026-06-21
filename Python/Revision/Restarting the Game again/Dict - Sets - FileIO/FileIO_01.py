f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present in poem.txt")
f.close()

with open("poem.txt","r") as f:
    c = f.read()
    if("twinkle" in c):
        print("Twinkle is present")

with open("Hiscore.txt","r") as f:
        hiscore = f.read() ##this always return string
        print(type(hiscore))
        print(int(hiscore) + 12) #type casting is required