english = int(input("Enter marks of English: "))
maths = int(input("Enter marks of Maths: "))
science = int(input("Enter marks of Science: "))
total_percentage = (english + maths + science)/3
if(total_percentage >40 and english >33 and science >33 and maths>33):
    print("You are passed",total_percentage)
else:
    print("Failed - Khatam - Tata - Bye Bye")