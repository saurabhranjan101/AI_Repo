with open("log.txt") as f:
    content = f.read()
if("python" in content):
    print("log file contain python")