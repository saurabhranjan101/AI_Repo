try:
    a = int(input("Enter a value os A -"))
except Exception as e:
    print(e)
else:
    print("I am inside else") #This runs only if
finally:
    print("This block always run")