maths = int(input("Enter marks of maths - "))
science = int(input("Enter marks of science - "))
english = int(input("Enter marks of english - "))

total = (maths+science+english)/3

if(total > 40):
    if(maths > 33 and science >33 and english > 33):
        print("Congratulations - You have passed")
else:
    print("Sorry - you have failed")