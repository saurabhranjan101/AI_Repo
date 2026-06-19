a = int(input("Enter a value of a -"))
b = int(input("Enter a value of b -"))
c = int(input("Enter a value of c -"))
d = int(input("Enter a value of d -"))
if(a>b and a>c and a>d):
    print("a is the greatest")
if(b>a and b>c and b>d):
    print("b is the greatest")
if(c>a and c>b and c>d):
    print("c is the greatest")
if(d>b and d>c and d>a):
    print("d is the greatest")