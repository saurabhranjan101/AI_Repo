with open("log.txt") as f:
    lines = f.readline()
lineno = 1
for line in lines:
    if("python" in line):
        print("log file contain python")
        break
    lineno += 1
else:
    print("Python is not present")