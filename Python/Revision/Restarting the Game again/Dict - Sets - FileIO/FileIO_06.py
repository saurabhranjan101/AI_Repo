with open("log.txt","r") as f:
    content = f.read()
    if("python" in content):
        print("python is present")
    else:
        print("python is not present")


##Print line number

line = 1
with open("log.txt","r") as f:
    lines = f.readline()
lineno = 1   
for line in lines:
    if("python" in line):
        print(f"Yes python is present in line number : {lineno}")
        lineno +=1
else:
    print("python is not present")
