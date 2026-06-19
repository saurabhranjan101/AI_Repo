n = int(input("Enter a number - ")) #n=5
for i in range(2,n): #i=2,3,4
    if(n%i==0):  #n=5 & i=2
        print(f"{n} Not a prime")
        break
else:
    print(f"{n} a Prime a number")