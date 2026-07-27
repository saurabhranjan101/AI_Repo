with open("joke.txt", "w") as f:
    f.write("Hello Mate! Hope all okk?")
with open("joke.txt", "r") as f:
    content = f.read()
    print(content) 