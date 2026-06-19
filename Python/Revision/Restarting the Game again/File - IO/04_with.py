f = open("file.txt")
data = f.read()
print(data)
f.close()

#Same we will write using with statement
print("============================")
with open("file.txt") as f:
    print(f.read())
#you don't have to explicitly close the file