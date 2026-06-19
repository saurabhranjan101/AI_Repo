def inchTocm(inch):
    return inch * 2.54
n = int(input("Enter a value in inch -"))
print(f"The corresponding value in cms is {inchTocm(n)}")