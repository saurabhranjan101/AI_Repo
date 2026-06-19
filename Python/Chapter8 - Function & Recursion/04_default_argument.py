def greet(name, ending = "Thank you"): ##This is default argument
    print(f"Hello {name}, Good Day!")
    print(ending)
greet("Saurabh") #This will take default value as we are not passing value for ending.
greet("Monu","Thanks") #This will take Thanks as an argument.