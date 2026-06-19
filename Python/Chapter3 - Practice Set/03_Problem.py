#Write a program to detect double space in a string.
name = "Saurabh is a  good boy"
print(name.find("  ")) # Output will retrn -1 if no double space. And return some other value if no doubel space.
print(name.replace("  "," "))

name1 = "Saurabh is a good boy"
print(name1.find("a")) 

name2 = "Saurabh is a good boy"
print(name2.count("a")) 