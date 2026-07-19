#write a python code to remove duplicate character from string

def duplicate(s):
    dup = " "
    for i in s:
        if( i in dup):
            pass
        else:
            dup += i
    return dup
s = input("Enter a string: ")
print("String after removing duplicate characters: ", duplicate(s))     