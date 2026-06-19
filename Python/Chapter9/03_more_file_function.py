# f = open("file.txt")
# lines = f.readlines() ##this return list and read all the lines.
# print(lines, type(lines))
# f.close()

# g = open("file.txt")
# line1 = g.readline() #Read each line
# line2 = g.readline()
# line3 = g.readline()
# line4 = g.readline()
# print(line1, type(line1)) #this will only print the first line
# print(line2, type(line2)) 
# print(line3, type(line3)) 
# print(line4, type(line4)) 
# g.close()

#Do above operation using while loop
f = open("file.txt")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()
