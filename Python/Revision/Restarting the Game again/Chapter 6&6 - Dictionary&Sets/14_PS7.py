d = {}
i = 0
while(i<4):
    Name = input("Enter your name - ")
    lang = input("Enter your favorite language - ")
    d.update({Name:lang})
    i+=1
print(d.items())