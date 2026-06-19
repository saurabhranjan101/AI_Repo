word = "Donkey"
with open("file1.txt","r") as f:
    content = f.read()
contentNew = content.replace(word,"######")

with open("file1.txt","w") as f:
    f.write(contentNew)