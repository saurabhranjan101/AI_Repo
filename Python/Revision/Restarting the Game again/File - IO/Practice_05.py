word = ["Donkey","ganda","bad"]
with open("file1.txt","r") as f:
    content = f.read()
for words in word:
    content = content.replace(words,"######")

with open("file1.txt","w") as f:
    f.write(content)