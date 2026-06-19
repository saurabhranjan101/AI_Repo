#Print multiplication table of a given number.
n = int(input("Enter a number - "))
i = 1
while(i < 11):
    print(f"{n}X{i} = {n*i}")
    i+=1