def main():
    try:
        a = int(input("Enter a value of A -"))
        return a
    except Exception as e:
        print(e)
        return
    else:
        print("I am inside else") #This runs only if try is successful
        return
    finally: ##this become effective when functions comees effective when function comes
        print("This block always run")
c = main()
print(c)