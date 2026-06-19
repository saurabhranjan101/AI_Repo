f = open("file.txt")
#lines = f.readlines() #This return list
# line1 = f.readline() #this return string
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# print(line1,type(line1))
# print(line2,type(line2))
# print(line3,type(line3))
# print(line4,type(line4))
# #print(lines,type(lines))
line = f.readline()
while(line !=""):
    print(line)
    line = f.readline()
f.close()