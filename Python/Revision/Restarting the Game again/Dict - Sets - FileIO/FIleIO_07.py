with open("this.txt","r") as f:
    content = f.read()
with open("this_new.txt","w") as f:
    f.write(content)

with open("this.txt","r") as f:
    content1 = f.read()
with open("this_new.txt","r") as g:
    content2 = g.read()
if(content1 == content2):
    print("Files are identical")

#wipeout the content of file
with open("wipe.txt","w") as h:
    h.write(" ")

#rename a file
with open("old.txt","r") as n:
    content = n.read()
with open("renamed_by_python.txt","w") as f:
    f.write(content)